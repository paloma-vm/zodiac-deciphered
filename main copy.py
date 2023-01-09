from flask import Flask, request, render_template
from dotenv import load_dotenv
import os
import requests
from flask_pymongo import PyMongo

load_dotenv()

app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb://localhost:27017/pollAnswers"
mongo = PyMongo(app)

@app.route('/')
def homepage():
    """A homepage for this site"""

    return render_template('home.html')

@app.route('/poll-results')
def poll_results():
    """A page to display the poll results"""

    return render_template('poll-results.html')




@app.route('/sketches')
def sketches():
    """A page about the details of Paul Doerr's sketches"""

    return render_template('sketches.html')

@app.errorhandler(404)
def page_not_found(error):
    """An error page for this site"""
    return render_template("404-error-page.html")

if __name__ == '__main__':
    app.config['ENV'] = 'development'
    app.run(debug=True)