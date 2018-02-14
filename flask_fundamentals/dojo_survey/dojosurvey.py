''' Assignment: Dojo Survey
Build a flask application that accepts a form submission, redirects, and presents the submitted data on a results page.
The goal is to help you get familiar with sending POST requests through a form and displaying that information. Consider the below example as a guide. '''

from flask import Flask, render_template, request, redirect
app = Flask(__name__)
@app.route('/') #our index.html page will handle rendering our form
def index():
    return render_template('index.html')
# this route will handle our form submission
# notice how we defined which HTTP methods are allowed by this route
@app.route('/result', methods=['POST'])
def display_user():
    print "Got Post Info"
    name = request.form['name']
    location = request.form['location']
    language = request.form['fav_language']
    comment = request.form['comment']
    print name, location, language, comment
    return render_template('result.html', name=request.form['name'], location=request.form['location'],language=request.form['fav_language'],comment=request.form['comment']) # Render the template and return it!

    # redirects back to the '/' route
    return redirect('/')

app.run(debug=True) # run our server    