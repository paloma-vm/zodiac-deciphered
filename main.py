from flask import Flask, request, redirect, render_template, url_for
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

@app.route('/poll', methods=['GET', 'POST'])
def update_poll():
    """A poll on this site"""
    if request.method == 'POST':

        new_poll_answer = {
            'users_answer': request.form.get('value')
        }

        result = mongo.db.answers.insert_one(new_poll_answer)
        return redirect(url_for('poll-results'))
    else:
        return render_template('poll.html')

@app.route('/poll-results', methods=['GET'])
def poll_results():
    """A page to display the poll results"""
    poll_data = mongo.db.answers.find()

    context = {
        'answers': poll_data
    }
    # find all yes answers
    yes_answers = mongo.db.answers.find({'users_answer': yes})
    # count the yes answers
    yes_count = len(yes_answers)
    # find all no answers
    no_answers = mongo.db.answers.find({'users_answer': no})
    # count the no answers
    no_count = len(no_answers)
     # find all no answers
    maybe_answers = mongo.db.answers.find({'users_answer': maybe})
    # count the maybe answers
    maybe_count = len(maybe_answers)


    return render_template('poll-results.html', **context)




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