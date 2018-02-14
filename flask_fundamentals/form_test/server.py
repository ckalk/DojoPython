from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'ThisIsSecret' # you need to set a secret key for security purposes

# our index route will handle rendering our form
@app.route('/')
def index():
  return render_template("index.html")

# this route will handle our form submission
# notice how we defined which HTTP methods are allowed 
@app.route('/process', methods=['POST'])
def create_user():
  print "Got Post Info"
  session['action'] = request.form['action']
  session['first_name'] = request.form['first_name']
  session['last_name'] = request.form['last_name']
  session['email'] = request.form['email']
  session['password'] = request.form['password']
  print session['action'] 

  if request.form['action'] == 'register':
    print "It's a registration"
    return redirect('/show/registration')
  elif request.form['action'] == 'login':
    print "It's a login"
    return redirect('/show/login')

  # redirects back to the '/' route
  #  return redirect('/')

@app.route('/show/<action>')
def show_user(action):
  print action
  # below is how we would pass session variables to the template
  # return render_template('user.html', name=session['name'], email=session['email'])
  # but we don't have to pass them, templates can call them directly
  return render_template('user.html', action=action)

app.run(debug=True) # run our server