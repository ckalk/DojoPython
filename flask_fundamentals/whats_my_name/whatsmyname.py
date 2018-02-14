''' Assignment: What's My Name?
Create a project that allows users to submit a form.
"/": renders a landing page with a form.
"/process": the route your form should submit to. In your process function, print the user's name and redirect to root. '''

from flask import Flask, render_template, request, redirect
app = Flask(__name__)
# our index route will handle rendering our form
@app.route('/')
def index():
  return render_template("index.html")
# this route will handle our form submission
# notice how we defined which HTTP methods are allowed by this route
@app.route('/process', methods=['POST'])
def process_data():
   print "Got Post Info"
   # we'll talk about the following two lines after we learn a little more
   # about forms
   name = request.form['name']
   email = request.form['email']
   print name, email
   print request.form
#    print request.form['name'], request.form['email'] find out why this doesn't work
   # redirects back to the '/' route
   return redirect('/')
   	 # Here's the line that changed. We're rendering a template from a post route now.
app.run(debug=True) # run our server