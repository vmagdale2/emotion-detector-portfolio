import requests
import os
from dotenv import load_dotenv

load_dotenv()  # Load .env file

API_URL = "https://api-inference.huggingface.co/models/bhadresh-savani/distilbert-base-uncased-emotion"
HEADERS = {"Authorization": f"Bearer {os.getenv('HF_API_KEY')}"}


def emotion_detector(text_to_analyze):
    """
    Analyze emotions in the input text using Hugging Face Inference API.

    Args:
        text_to_analyze (str): The input text to analyze.

    Returns:
        dict: Dictionary of emotion scores and dominant emotion.
    """
    if not text_to_analyze or not text_to_analyze.strip():
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    payload = {"inputs": text_to_analyze}
    print("API key loaded:", os.getenv('HF_API_KEY')[:4], "...")
    print("Sending text:", text_to_analyze)
    response = requests.post(API_URL, headers=HEADERS, json=payload)
    print("API response:", response.status_code, response.text)
    if response.status_code != 200:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    predictions = response.json()[0]

    # Normalize and convert Hugging Face labels to match our previous style
    label_map = {
        'anger': 'anger',
        'joy': 'joy',
        'sadness': 'sadness',
        'fear': 'fear',
        'disgust': 'disgust',   # Not returned, will be set to 0
        'love': 'joy',          # Combine with joy
        'surprise': 'joy'       # Combine with joy
    }

    emotions = {
        'anger': 0.0,
        'disgust': 0.0,
        'fear': 0.0,
        'joy': 0.0,
        'sadness': 0.0
    }

    for pred in predictions:
        label = label_map.get(pred["label"].lower())
        if label:
            emotions[label] += pred["score"]

    dominant_emotion = max(emotions, key=emotions.get)

    emotions['dominant_emotion'] = dominant_emotion
    return emotions
