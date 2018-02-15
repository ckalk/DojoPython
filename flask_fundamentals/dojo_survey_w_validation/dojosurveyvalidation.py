''' Assignment: Dojo Survey With Validation
Take the Dojo Survey assignment that you completed previously and add validations:
* Name and Comment fields should be validated so that they are not blank. 
* Also, validate that the comment field is no longer than 120 characters. '''

from flask import Flask, render_template, redirect, request, session, flash
app = Flask(__name__)
app.secret_key = 'KeepItSecretKeepItSafe'

# the "re" module will let us perform some regular expression operations
# import re
# create a regular expression object that we can use run operations on
# EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

@app.route('/') 
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def display_user():
    print "Got Post Info"
    name = request.form['name']
    location = request.form['location']
    language = request.form['fav_language']
    comment = request.form['comment']
    print name, location, language, comment
#validate that the name field is not empty 
    if len(request.form['name']) < 1:
        flash("Name field cannot be empty!")
    else:
        flash("Success! Your name field is {}.".format(request.form['name']))
#validate that the comment field is not empty   
    if len(request.form['comment']) < 1:
        flash("Comment field cannot be empty!")
# validate that the comment field is no longer than 120 characters
    elif len(request.form['comment']) > 120:
        flash("Comment field cannot be longer than 120 characters.")
    else:
        flash("Success! Your comment field ({}) is less than 120 characters.".format(request.form['comment']))

    return render_template('result.html', name=request.form['name'], location=request.form['location'],language=request.form['fav_language'],comment=request.form['comment']) 

    # redirects back to the '/' route
    return redirect('/')

app.run(debug=True) # run our server    