# Minimal LLM client wrapper - placeholder for LangChain/Gemini integration

class LLMClient:
    def __init__(self, api_key: str | None = None):
        self.api_key = api_key

    async def generate(self, prompt: str) -> str:
        # Placeholder: integrate with LangChain and Gemini LLM
        return "generated response"
