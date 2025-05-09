NLP Preprocessing Demo
This project demonstrates core NLP preprocessing techniques, including tokenization, lemmatization, stemming, POS tagging, and Named Entity Recognition (NER) using NLTK and spaCy libraries.
Features

Tokenization using both NLTK and spaCy
Lemmatization for converting words to their base forms
Stemming for reducing words to their stems
Part-of-Speech (POS) tagging
Named Entity Recognition (NER)
Interactive comparison between lemmatization and stemming
RESTful API for all NLP functions
User-friendly web interface

Project Structure

app.py: Flask backend with all NLP preprocessing functions
index.html: Frontend web interface
requirements.txt: Python dependencies

Setup Instructions
1. Create a virtual environment
bashpython -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
2. Install dependencies
bashpip install -r requirements.txt
3. Download spaCy model
bashpython -m spacy download en_core_web_sm
4. Run the Flask application
bashpython app.py
The server will start on http://localhost:5000
5. Open the web interface
Open index.html in your web browser. You can either:

Open the file directly from your file explorer
Serve it using a simple HTTP server:
bash# Python 3
python -m http.server
Then navigate to http://localhost:8000

API Endpoints
The following RESTful API endpoints are available:

POST /api/tokenize: Tokenize input text
POST /api/lemmatize: Lemmatize input text
POST /api/stem: Stem input text
POST /api/pos_tag: Perform POS tagging on input text
POST /api/ner: Perform Named Entity Recognition on input text
POST /api/compare: Compare stemming and lemmatization for a list of words
POST /api/process_all: Process text with all methods at once

Lemmatization vs. Stemming
The application includes a comparison tool that demonstrates the differences between lemmatization and stemming:

Stemming:

Removes word endings using fixed rules
Faster but less accurate
Often produces non-dictionary words
Rule-based approach


Lemmatization:

Reduces words to their dictionary base form (lemma)
Uses vocabulary and morphological analysis
Considers context and part of speech
Slower but more accurate
Always produces valid dictionary words



Example differences:

"running" → Stem: "run", Lemma: "running" (as noun) or "run" (as verb)
"better" → Stem: "better", Lemma: "good" (as adjective) or "better" (as adverb)
"wolves" → Stem: "wolv", Lemma: "wolf"
"studies" → Stem: "studi", Lemma: "study"

Requirements

Python 3.6+
Modern web browser with JavaScript enabled