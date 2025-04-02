"""Flask web app to detect emotions from text using IBM Watson NLP."""
import logging
from datetime import datetime
from flask import Flask, request, render_template
from EmotionDetection import emotion_detector

app = Flask(__name__)

# Create logs directory if it doesn't exist
import os
if not os.path.exists("logs"):
    os.mkdir("logs")

log_filename = f"logs/emotion_app_{datetime.now().strftime('%Y-%m-%d')}.log"

logging.basicConfig(
    filename=log_filename,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

@app.route('/')
def index():
    """Render the index page with the input form."""
    return render_template('index.html')

@app.route('/emotionDetector', methods=['GET', 'POST'])
def emotion_detect_route():
    """
    Handle emotion detection request and return formatted results in HTML.
    """
    if request.method == 'POST':
        text_to_analyze = request.form.get('textToAnalyze')
    else:
        text_to_analyze = request.args.get('textToAnalyze')

    result = emotion_detector(text_to_analyze)

    if result['dominant_emotion'] is None:
        return render_template("index.html", error="Invalid text! Please try again.")

    return render_template("index.html", result=result, text=text_to_analyze)
    logging.info(f"User input: {text_to_analyze}")
    logging.info(f"Detected emotions: {result}")
    if result['dominant_emotion'] is None:
        logging.warning("Invalid input detected — no dominant emotion.")
        return render_template("index.html", error="Invalid text! Please try again.")

if __name__ == '__main__':
    app.run(debug=True, port=5000)