import os
import google.generativeai as genai
from django.conf import settings

api_key = getattr(settings, 'GEMINI_API_KEY', None) or os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("GEMINI_API_KEY environment variable is not set")
genai.configure(api_key=api_key)

MODEL = "gemini-2.5-flash"

def generate_post_content(platform: str, context_term: str) -> str:
    prompt = f"""
        You are a copywriting assistant.

        TASK:
        Write a {platform} caption about "{context_term}" focused on mindset and growth.

        RULES:
        - Exactly 2 sentences
        - Each sentence max 15 words
        - No emojis
        - No hashtags
        - No explanations
        - No line breaks
        - Output only the caption text

        OUTPUT:
"""

    model = genai.GenerativeModel(MODEL)

    response = model.generate_content(prompt)

    return response.text.strip()
