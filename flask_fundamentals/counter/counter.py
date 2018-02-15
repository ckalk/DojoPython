''' Assignment: Counter
Build a flask application that counts the number of times the root route ('/') has been viewed. 
This assignment is to test your understanding of session.
* Ninja Level 1: Add a +2 button underneath the counter that reloads the page and increments counter by 2. Add another route to handle this functionality.
* Ninja Level 2: Add a reset button that resets the counter back to 1. Add another route to handle this functionality. '''

from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'ThisIsSecret' # you need to set a secret key for security purposes

first = "true"
@app.route('/')
def index():
  if 'cntr' not in session:
    session['cntr']=0
  return render_template("index.html")

@app.route('/addtocount', methods=['POST'])
def count():
  print "Got Post Info"
  session['cntr']+=1
  print session['cntr']
  return redirect('/')

@app.route('/add2tocount', methods=['POST'])
def add2tocount():
  print "Got Post Info"
  session['cntr']+=2
  print session['cntr']
  return redirect('/')

@app.route('/resetctr', methods=['POST'])
def resetctr():
  print "Got Post Info"
  session['cntr'] = 0
  print session['cntr']
  return redirect('/')

app.run(debug=True) # run our server