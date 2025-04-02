# 🧠 Emotion Detector App

A web-based emotion detection app that analyzes user-submitted text and identifies the emotional content using machine learning. The application uses a Hugging Face Inference API model to predict emotions such as joy, anger, sadness, fear, and more.

---

## 🌐 Live Demo

🔗 [Try the live app on Render](https://emotion-detector-yw6l.onrender.com)

---

## 💡 Features

- 🗞 Analyze any text and detect top 5 emotions
- 🎯 Returns emotion scores and highlights the dominant one
- 🌈 Clean, responsive Bootstrap UI
- 🧪 Built-in unit tests for model reliability
- �� Logging of user inputs and detected emotions
- ☁️ Publicly deployed with Render
- 🔒 Hugging Face API key securely loaded via `.env`

---

## 🛠️ Tech Stack

| Layer         | Technology                              |
|---------------|------------------------------------------|
| Frontend      | HTML5, Bootstrap 5                       |
| Backend       | Python, Flask                            |
| Model API     | Hugging Face Inference (`distilbert-base-uncased-emotion`) |
| Deployment    | Render.com                               |
| Testing       | unittest (Python stdlib)                 |
| Logging       | Python logging module                    |

---

## 📸 Screenshots

![Emotion Output Card](screenshots/emotion_results.png) <!-- Replace with your own screenshots -->

---

## 🚀 Getting Started (Local)

### 1. Clone the Repository

```bash
git clone https://github.com/vmagdale2/emotion-detector-portfolio.git
cd emotion-detector-portfolio
```

### 2. Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate      # On Windows
# OR
source venv/bin/activate   # On Mac/Linux
```

### 3. Install Requirements

```bash
pip install -r requirements.txt
```

### 4. Create `.env` File

Create a `.env` file in the root directory:

```env
HF_API_KEY=your_huggingface_token_here
```

### 5. Run the App

```bash
python server.py
```

Open browser: [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 🧪 Run Unit Tests

```bash
python -m unittest test_emotion_detection.py
```

---

## ☁️ Deploy to Render (Optional)

- Push to GitHub
- Connect repo on [https://render.com](https://render.com)
- Use `gunicorn server:app` as Start Command
- Add your Hugging Face API key as an environment variable

---

## 🙌 Acknowledgments

- 🤗 [Hugging Face Model](https://huggingface.co/bhadresh-savani/distilbert-base-uncased-emotion)
- 💙 Coursera x IBM - Emotion Detection Project Prompt

---

## 👩‍💼 Author

**Veronica Magdaleno**  
💼 [LinkedIn](https://www.linkedin.com/in/veronica-magdaleno-84248862/)  
🧪 Data Scientist | Flask Dev | AI Enthusiast  
📬 jobsearchvmagda@gmail.com

---

## ⭐ Like This Project?

Give it a ⭐ on GitHub or share it with someone who’s interested in emotion detection with NLP!

