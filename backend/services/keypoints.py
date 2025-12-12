# backend/services/keypoints.py
import os
import google.generativeai as genai
import logging

logger = logging.getLogger(__name__)
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

def generate_pros_cons(text: str) -> str:
    if not GEMINI_API_KEY:
        return "API Key Gemini tidak ditemukan."

    try:
        genai.configure(api_key=GEMINI_API_KEY)
        model = genai.GenerativeModel("gemini-pro")
        
        # Prompt yang diubah total agar outputnya terstruktur
        prompt = (
            f"Analisis teks ulasan berikut: \"{text}\".\n"
            "Identifikasi kelebihan dan kekurangannya. "
            "Berikan output dalam format Bahasa Indonesia yang rapi seperti ini:\n\n"
            "✅ KELEBIHAN:\n- [Poin 1]\n- [Poin 2]\n\n"
            "❌ KEKURANGAN:\n- [Poin 1]\n- [Poin 2]"
        )
        
        response = model.generate_content(prompt)
        return response.text if response.text else "Tidak ada hasil analisis."
    
    except Exception as e:
        logger.error(f"Gemini Error: {e}")
        return "Gagal melakukan analisis AI."