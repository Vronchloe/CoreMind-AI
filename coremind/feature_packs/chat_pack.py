class ChatFeaturePack:
    """Basic conversational AI feature pack"""
    
    def __init__(self, engine):
        self.engine = engine
        self.name = "Chat Assistant"
    
    def process(self, user_input: str) -> str:
        context = "You are CoreMind AI, a helpful offline assistant."
        return self.engine.generate_response(user_input, context)
