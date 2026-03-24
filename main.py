"""
Email Tone Analyzer - Main Application File
This script sets up a Flask web server and uses TextBlob for NLP sentiment analysis.
"""

from flask import Flask, render_template, request
from textblob import TextBlob

# Initialize the Flask application environment
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    """
    Route handling for the main page.
    Accepts GET requests to display the page, and POST requests to analyze submitted text.
    """
    tone_result = None
    user_text = ""
    
    if request.method == 'POST':
        # Retrieve the email draft text submitted by the user
        user_text = request.form['email_text']
        
        # Initialize TextBlob to process the natural language
        analysis = TextBlob(user_text)
        
        # Extract the polarity score (ranges from -1.0 to 1.0)
        polarity = analysis.sentiment.polarity
        
        # Classify the tone based on the polarity score
        if polarity > 0.1:
            tone_result = "Positive / Friendly 😊"
        elif polarity < -0.1:
            tone_result = "Negative / Aggressive 😠"
        else:
            tone_result = "Neutral 😐"
            
    # Render the HTML template and pass the variables to the frontend
    return render_template('index.html', tone_result=tone_result, user_text=user_text)

if __name__ == '__main__':
    # Run the Flask server locally on port 5000
    app.run(host='0.0.0.0', port=5000)
