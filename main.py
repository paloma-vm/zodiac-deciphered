from flask import Flask, request, redirect, render_template, url_for
from dotenv import load_dotenv
import os
import requests
from flask_pymongo import PyMongo

load_dotenv()

app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb://localhost:27017/zodiacPollAnswers"
mongo = PyMongo(app)

@app.route('/')
def homepage():
    """A homepage for this site"""
    
    return render_template('home.html')

@app.route('/poll', methods=['GET', 'POST'])
def update_poll():
    """A poll on this site"""
    print('/poll *****************')
    if request.method == 'POST':
        # get user's answer and store it in the object new_poll_answer
        new_poll_answer = {
            'users_answer': request.form.get('user_answer')
        }
        print(request.form.get('user_answer'))
        # insert object into answers database
        result = mongo.db.answers.insert_one(new_poll_answer)
        print('___________________')
        print(new_poll_answer)

        return redirect(url_for('poll_results'))#name of the function
    else:
        return render_template('poll.html')

@app.route('/poll-results', methods=['GET', 'POST'])
def poll_results():
    """A page to display the poll results"""
    print('/poll-results *********************')
  
    poll_data = mongo.db.answers.find() #do I need this?  I don't think so.
    

   
    # find all yes answers
    yes_answers = mongo.db.answers.find({'users_answer': 'yes'})

 
    # count the yes answers
    yes_answers_count = len(list(yes_answers))

    print('~~~~~~~~~~~~~~~~')
    print(yes_answers_count)

    # find all no answers
    no_answers = mongo.db.answers.find({'users_answer': 'no'})
    # count the no answers
    no_answers_count = len(list(no_answers))
    print('~~~~~~~~~~~~~~~~')
    print(no_answers_count)
     # find all maybe answers
    maybe_answers = mongo.db.answers.find({'users_answer': 'maybe'})
    # count the maybe answers
    maybe_answers_count = len(list(maybe_answers))
    print('~~~~~~~~~~~~~~~~')
    print(maybe_answers_count)

    context = {
        'yes_answers_count': yes_answers_count,
        'no_answers_count': no_answers_count,
        'maybe_answers_count': maybe_answers_count,

    }


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