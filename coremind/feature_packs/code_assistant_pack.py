class CodeAssistantPack:
    """Code analysis and debugging feature pack"""
    
    def __init__(self, engine):
        self.engine = engine
        self.name = "Code Assistant"
    
    def process(self, code: str, question: str = "") -> str:
        context = "You are a code assistant. Analyze the following code and provide insights."
        prompt = f"Code:\n{code}\n\nQuestion: {question}"
        return self.engine.generate_response(prompt, context)
