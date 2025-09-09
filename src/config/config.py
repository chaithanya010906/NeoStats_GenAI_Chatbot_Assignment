import os

# Load API key from environment
GROQ_API_KEY = os.getenv("GROQ_API_KEY", "")

# Default chatbot settings
DEFAULT_SYSTEM_PROMPT = "You are a helpful AI assistant."
DEFAULT_MODEL = "llama-3.1-8b-instant"
