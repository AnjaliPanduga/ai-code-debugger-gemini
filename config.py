import os
from dotenv import load_dotenv
import google.generativeai as genai

def configure_api():
    load_dotenv()
    api_key = os.getenv("GOOGLE_API_KEY")
    genai.configure(api_key=api_key)