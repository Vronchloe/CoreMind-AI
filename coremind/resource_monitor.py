import psutil
import platform

class ResourceMonitor:
    """Monitors CPU, RAM, and determines optimal model configuration"""
    
    def __init__(self):
        self.system_info = self.get_system_info()
    
    def get_system_info(self) -> dict:
        """Get basic system information"""
        return {
            "os": platform.system(),
            "cpu_count": psutil.cpu_count(),
            "total_ram_gb": round(psutil.virtual_memory().total / (1024**3), 2)
        }
    
    def get_current_usage(self) -> dict:
        """Get real-time resource usage"""
        cpu_percent = psutil.cpu_percent(interval=1)
        memory = psutil.virtual_memory()
        
        return {
            "cpu_usage": cpu_percent,
            "ram_used_gb": round(memory.used / (1024**3), 2),
            "ram_available_gb": round(memory.available / (1024**3), 2),
            "ram_percent": memory.percent
        }
    
    def recommend_model(self) -> str:
        """Recommend model based on available resources"""
        usage = self.get_current_usage()
        available_ram = usage["ram_available_gb"]
        
        if available_ram > 8:
            return "llama3.2:1b (Full Model)"
        elif available_ram > 4:
            return "llama3.2:1b (Quantized 8-bit)"
        else:
            return "llama3.2:1b (Quantized 4-bit)"
    
    def get_health_status(self) -> str:
        """Overall system health for AI processing"""
        usage = self.get_current_usage()
        
        if usage["ram_percent"] < 70 and usage["cpu_usage"] < 80:
            return "OPTIMAL"
        elif usage["ram_percent"] < 85 and usage["cpu_usage"] < 90:
            return "MODERATE"
        else:
            return "CONSTRAINED"
