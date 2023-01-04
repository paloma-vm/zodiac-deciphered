from flask import Flask, request, render-template
from dotenv import load_dotenv

import requests

load_dotenv()

app = Flask(__name__)

@app.route('/')
def homepage():
    """A homepage for this site"""
    return render_template('home.html')

if __name__ == '__main__':
    app.config['ENV'] = 'development'
    app.run(debug=True)