import os
from dotenv import load_dotenv

load_dotenv()

# Get the API key from the environment variable
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GEMINI_MODEL = os.getenv("GEMINI_MODEL")

if not GEMINI_API_KEY or not GEMINI_MODEL:
    raise ValueError("❌ API key not found. Set GEMINI_API_KEY and GEMINI_MODEL in the .env file.")