import google.generativeai as genai
from config.config import GEMINI_API_KEY, GEMINI_MODEL

# Configure the Gemini API
genai.configure(api_key=GEMINI_API_KEY)
# Load the Gemini model
model = genai.GenerativeModel(GEMINI_MODEL)
