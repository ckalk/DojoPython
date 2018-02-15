''' Assignment: Great Number Game
Create a site that when a user loads it creates a random number between 1-100 and stores the number in session. Allow the user to guess at the number and tell them when they are too high or too low. If they guess the correct number tell them and offer to play again.
In order to generate a random number you can use the "random" python module.
In order to remove something from the session, you must "pop" it off of the session dictionary. '''

from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'ThisIsSecret' # you need to set a secret key for security purposes

import random

@app.route('/')
def index():
    session['curr_random'] = random.randint(1, 100)
    print  session['curr_random']
    return render_template("index.html")

@app.route('/returnguess', methods=['POST'])
def returnguess():
    print  request.form['guess']
    session['guess'] = int(request.form['guess'])
    return render_template("result.html")

@app.route('/correctguess', methods=['POST'])
def correctguess():
    print session
    print request.form['playagain']
    if request.form['playagain'] == 'yes':
        return redirect('/')
    else:
        return render_template("gameover.html")

app.run(debug=True) # run our server