from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import spacy
import nltk
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.tokenize import word_tokenize

# Download required NLTK resources
nltk.download('punkt', quiet=True)
nltk.download('wordnet', quiet=True)
nltk.download('averaged_perceptron_tagger', quiet=True)
nltk.download('maxent_ne_chunker', quiet=True)
nltk.download('words', quiet=True)

# Load spaCy model
try:
    nlp = spacy.load('en_core_web_sm')
except OSError:
    import spacy.cli
    spacy.cli.download('en_core_web_sm')
    nlp = spacy.load('en_core_web_sm')

# Initialize NLTK components
stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/tokenize', methods=['POST'])
def tokenize():
    data = request.json
    text = data.get('text', '')
    
    doc = nlp(text)
    return jsonify({
        'nltk_tokens': word_tokenize(text),
        'spacy_tokens': [token.text for token in doc]
    })

@app.route('/api/lemmatize', methods=['POST'])
def lemmatize():
    data = request.json
    text = data.get('text', '')
    
    doc = nlp(text)
    return jsonify({
        'nltk_lemmas': [lemmatizer.lemmatize(word) for word in word_tokenize(text)],
        'spacy_lemmas': [token.lemma_ for token in doc]
    })

@app.route('/api/stem', methods=['POST'])
def stem():
    data = request.json
    text = data.get('text', '')
    return jsonify({
        'stems': [stemmer.stem(word) for word in word_tokenize(text)]
    })

@app.route('/api/pos_tag', methods=['POST'])
def pos_tag():
    data = request.json
    text = data.get('text', '')
    
    doc = nlp(text)
    return jsonify({
        'nltk_pos_tags': nltk.pos_tag(word_tokenize(text)),
        'spacy_pos_tags': [(token.text, token.pos_) for token in doc]
    })

@app.route('/api/ner', methods=['POST'])
def ner():
    data = request.json
    text = data.get('text', '')
    
    doc = nlp(text)
    return jsonify({
        'entities': [{
            'text': ent.text,
            'label': ent.label_,
            'start': ent.start_char,
            'end': ent.end_char
        } for ent in doc.ents]
    })

@app.route('/api/process_all', methods=['POST'])
def process_all():
    data = request.json
    text = data.get('text', '')
    
    doc = nlp(text)
    return jsonify({
        'tokens': [token.text for token in doc],
        'lemmas': [token.lemma_ for token in doc],
        'stems': [stemmer.stem(token.text) for token in doc],
        'pos_tags': [(token.text, token.pos_) for token in doc],
        'entities': [{'text': ent.text, 'label': ent.label_} for ent in doc.ents]
    })

if __name__ == '__main__':
    app.run(debug=True)