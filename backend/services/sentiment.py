# backend/services/sentiment.py
import os
import logging
import httpx

logger = logging.getLogger(__name__)
HF_API_KEY = os.getenv("HF_API_KEY")
HF_MODEL = "https://api-inference.huggingface.co/models/cardiffnlp/twitter-roberta-base-sentiment"

async def analyze_sentiment_text(text: str) -> str:
    if not HF_API_KEY:
        return "unknown"

    headers = {"Authorization": f"Bearer {HF_API_KEY}"}
    payload = {"inputs": text}

    try:
        async with httpx.AsyncClient(timeout=10.0) as client:
            response = await client.post(HF_MODEL, headers=headers, json=payload)
        
        if response.status_code != 200:
            logger.error(f"HF Error: {response.text}")
            return "neutral"

        data = response.json()
        # Parsing response Hugging Face yang kadang berupa list of list
        try:
            if isinstance(data, list) and len(data) > 0:
                if isinstance(data[0], list):
                    label = data[0][0]['label']
                else:
                    label = data[0]['label']
                
                # Normalisasi label
                label = label.lower()
                if "label_0" in label or "neg" in label: return "negative"
                if "label_2" in label or "pos" in label: return "positive"
                return "neutral"
        except (KeyError, IndexError, TypeError):
            return "neutral"

        return "neutral"

    except Exception as e:
        logger.error(f"Sentiment service error: {e}")
        return "error"