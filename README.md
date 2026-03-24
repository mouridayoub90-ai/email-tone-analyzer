# email-tone-analyzer
# 📧 Email Tone Analyzer

This is a web application built with Python, HTML, and CSS. It analyzes the text of an email draft and uses AI sentiment analysis to determine if the tone is Positive, Negative, or Neutral. 

## 🚀 Live Demo
https://email-tone-analyzer--yassineroundi-e.replit.app

## 🛠️ Built With
* **Python (Flask):** Handles the backend server and routing.
* **TextBlob:** Python library used for Natural Language Processing (NLP) to analyze the sentiment.
* **HTML/CSS:** Creates a clean, responsive user interface.

## 💻 How It Works
1. The user pastes an email draft into the text box.
2. The form submits a `POST` request to the Flask backend.
3. `TextBlob` analyzes the text's polarity (from -1.0 to 1.0).
4. The website returns a result: Positive, Negative, or Neutral.
