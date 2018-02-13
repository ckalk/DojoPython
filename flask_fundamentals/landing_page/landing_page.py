''' Assignment: Landing Page
Create a flask project capable of handling the following routes.
localhost:5000/    This route should serve a view file called index.html and display a greeting. This will be considered our 'root route'.
localhost:5000/ninjas    This route should serve a view file called ninjas.html and display information about ninjas.
localhost:5000/dojos/new    This route should serve a view file called dojos.html and have a form. Don't worry where the form should be sent to for now, you can simply set your action blank, like this:action=''. '''

from flask import Flask, render_template  # Import Flask to allow us to create our app, and import
                                          # render_template to allow us to render html pages
app = Flask(__name__)                     # Global variable __name__ tells Flask whether or not we
                                          # are running the file directly or importing it as a module.
@app.route('/')                           # The "@" symbol designates a "decorator" which attaches the
                                          # following function to the '/' route. This means that
                                          # whenever we send a request to localhost:5000/ we will run
                                          # the following function.
def index():
    return render_template('index.html')    # Render the template and return it!

@app.route('/ninjas')
def ninjas():
    return render_template('ninjas.html')

@app.route('/dojos/new')  
def dojos():
    return render_template('dojos.html')

  
app.run(debug=True) 
