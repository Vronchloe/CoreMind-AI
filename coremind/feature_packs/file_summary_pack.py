class FileSummaryPack:
    """Document summarization feature pack"""
    
    def __init__(self, engine):
        self.engine = engine
        self.name = "File Summarizer"
    
    def process(self, text: str) -> str:
        context = "Summarize the following text concisely."
        return self.engine.generate_response(text, context)
