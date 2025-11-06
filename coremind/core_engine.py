import requests
import json
from typing import Dict, Optional

class CoreMindEngine:
    """Main AI engine for CoreMind - handles offline inference via Ollama"""
    
    def __init__(self, model_name: str = "llama3.2:1b"):
        self.model_name = model_name
        self.ollama_url = "http://localhost:11434"
        self.feature_packs = {}
        
    def check_ollama_status(self) -> bool:
        """Check if Ollama is running locally"""
        try:
            response = requests.get(f"{self.ollama_url}/api/tags", timeout=2)
            return response.status_code == 200
        except:
            return False
    
    def generate_response(self, prompt: str, context: str = "") -> str:
        """Generate AI response completely offline"""
        if not self.check_ollama_status():
            return "Error: Ollama not running. Please start Ollama service."
        
        full_prompt = f"{context}\n{prompt}" if context else prompt
        
        try:
            response = requests.post(
                f"{self.ollama_url}/api/generate",
                json={
                    "model": self.model_name,
                    "prompt": full_prompt,
                    "stream": False
                },
                timeout=30
            )
            
            if response.status_code == 200:
                return response.json()["response"]
            else:
                return f"Error: {response.status_code}"
                
        except Exception as e:
            return f"Error generating response: {str(e)}"
    
    def load_feature_pack(self, pack_name: str, pack_module):
        """Dynamically load a feature pack module"""
        self.feature_packs[pack_name] = pack_module
        print(f"✓ Feature Pack '{pack_name}' loaded")
    
    def unload_feature_pack(self, pack_name: str):
        """Remove a feature pack"""
        if pack_name in self.feature_packs:
            del self.feature_packs[pack_name]
            print(f"✗ Feature Pack '{pack_name}' unloaded")
    
    def list_feature_packs(self) -> list:
        """Return list of active feature packs"""
        return list(self.feature_packs.keys())
