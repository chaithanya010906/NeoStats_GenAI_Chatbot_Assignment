from groq import Groq
from src.config.config import GROQ_API_KEY, DEFAULT_MODEL, DEFAULT_SYSTEM_PROMPT

class LLM:
    def __init__(self, api_key=GROQ_API_KEY, model=DEFAULT_MODEL, system_prompt=DEFAULT_SYSTEM_PROMPT):
        if not api_key:
            raise ValueError("❌ Missing GROQ_API_KEY. Please set it in environment variables.")
        self.client = Groq(api_key=api_key)
        self.model = model
        self.system_prompt = system_prompt

    def chat(self, user_message, temperature=0.5):
        """Send user message to Groq LLM and get response"""
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": self.system_prompt},
                    {"role": "user", "content": user_message},
                ],
                temperature=temperature,
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"⚠️ Error: {str(e)}"
