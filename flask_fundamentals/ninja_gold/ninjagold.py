''' Assignment: Ninja Gold -- Create a simple game to test your understanding of flask, and implement the functionality below.
When you start the game, your ninja should have 0 gold. 
* The ninja can go to different places (farm, cave, house, casino) and earn different amounts of gold. 
* Casino, your ninja can earn or LOSE up to 50 golds. 
Your job is to create a web app that allows this ninja to earn gold and to display past activities of this ninja.
Refer to the wireframe below.
Have the four forms appear when the user goes to http://localhost:5000.
For the farm, your form would look something like
    <form action="/process_money" method="post">
      <input type="hidden" name="building" value="farm" />
      <input type="submit" value="Find Gold!"/>
    </form>
    In other words, you want to include a hidden value in the form and have each form submit the form information to /process_money.
    Have /process_money determine how much gold the user should have.
    You should only have 2 routes -- '/' and '/process_money' (reset can be another route if you implement this feature). '''

from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'ThisIsSecret' # you need to set a secret key for security purposes

import random
import datetime 

now = datetime.datetime.now() 
today = now.strftime("%Y-%m-%d %I:%M %p")
print today

@app.route('/')
def index():
    if 'yourgold' not in session:
        session['yourgold'] = 0
        session['activities'] = []
    
    return render_template('index.html')

@app.route('/process_money', methods=['POST'])
def process_money():
    print session['yourgold']
    print request.form['building']
    now = datetime.datetime.now() 
    today = now.strftime("%Y-%m-%d %I:%M %p")
    print today

    if request.form['building'] == 'farm':
        newgold = random.randint(10, 20)
        session['newgold'] = newgold
        activity = 'Earned {} golds from the farm! ({})'.format(newgold, today)
        print activity
        session['activities'].insert(0,activity)
    elif request.form['building'] == 'cave':
        newgold = random.randint(5, 10)
        session['newgold'] = newgold
        activity = 'Earned {} golds from the cave! ({})'.format(newgold, today)
        print activity
        session['activities'].insert(0,activity)
    elif request.form['building'] == 'house':
        newgold = random.randint(2, 5)
        session['newgold'] = newgold
        activity = 'Earned {} golds from the house! ({})'.format(newgold, today)
        print activity
        session['activities'].insert(0,activity)
    else:
        newgold = random.randint(-50, 50)
        session['newgold'] = newgold
        if newgold >= 0:
            activity = 'Yay! You earned {} gold from the casino! ({})'.format(newgold, today)
        else:
            activity = 'Entered a casino and lost {} golds...Ouch... ({})'.format(newgold, today)
        print activity
        session['activities'].insert(0,activity)

    session['yourgold'] = session['yourgold']+session['newgold']

    print session['newgold']
    print session['yourgold']
    print session['activities']

    return redirect('/')

@app.route('/reset', methods=['POST'])
def resest():
    if session:
        session.clear()
    
    return redirect('/')
  
app.run(debug=True) 