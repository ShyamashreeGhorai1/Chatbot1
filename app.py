from flask import Flask, render_template, request,jsonify
from flask_cors import CORS
import google.generativeai as genai
from config import GEMINI_API_KEY
import json

app = Flask(__name__)

app.config['MAX_CONTENT_LENGTH'] = 16*1024*1024
CORS(app)

genai.config(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-2.0-flash')
@app.route('/')
def index():
    return render_template('index.html')
