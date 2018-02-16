''' Assignment: Registration Form -- Create a simple registration page with the following fields:
email, first_name, last_name, password, confirm_password
Here are the validations you must include:
* All fields are required and must not be blank
* First and Last Name cannot contain any numbers
* Password should be more than 8 characters
* Email should be a valid email
* Password and Password Confirmation should match
--When the form is submitted, make sure the user submits appropriate information. If the user did not submit appropriate information, return the error(s) above the form that asks the user to correct the information. 
--Message Flashing with Categories
For this, you will need to use flash messages at the very least. You may have to take this one step further and add categories to the flash messages.
If the form with all the information is submitted properly, simply have it say a message "Thanks for submitting your information."
--Ninja Version: Add the validation that requires a password to have at least 1 uppercase letter and 1 numeric value.
--Hacker Version: Add a birth-date field that must be validated as a valid date and must be from the past. '''

from flask import Flask, render_template, redirect, request, session, flash
app = Flask(__name__)
app.secret_key = 'KeepItSecretKeepItSafe'

# the "re" module will let us perform some regular expression operations
import re
# create a regular expression object that we can use run operations on
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

''' NAME_REGEX Check for no numbers like this: ^[^0-9]+$
Explanation:
    ^ matches the beginning of the string
    [^...] matches anything that isn't inside
    0-9 means any character between 0 and 9
    + matches one or more of the previous thing
    $ matches the end of the string '''
NAME_REGEX = re.compile(r'^[^0-9]+$')


# if PASSWORD_REGEX match is true ==> NOT at least one uppercase and at least one number
PASSWORD_REGEX = re.compile(r'^([^0-9]*|[^A-Z]*)$')

DATE_REGEX = re.compile(r'^\d{4}\-(0?[1-9]|1[012])\-(0?[1-9]|[12][0-9]|3[01])$')

import datetime 

now = datetime.datetime.now() 
today = now.strftime("%Y-%m-%d")
print today

@app.route('/') 
def index():
    return render_template('index.html')

@app.route('/validate', methods=['POST'])
def validate():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    birth_date = request.form['birth_date']
    email = request.form['email']
    password = request.form['password']
    confirm_pwd = request.form['confirm_pwd']
    print first_name, last_name, birth_date, email, password, confirm_pwd

#validate each field; add flash msg if fails validation
    if len(first_name) < 1:
        flash("You must enter your first name.",'error')
    elif not NAME_REGEX.match(request.form['first_name']):
        flash("Invalid characters in first name.",'error')
    
    if len(last_name) < 1:
        flash("You must enter your last name.",'error')
    elif not NAME_REGEX.match(request.form['last_name']):
        flash("Invalid characters in last name.",'error')
    
    if len(birth_date) < 1:
        flash("You must enter a birth date.",'error')
    elif not DATE_REGEX.match(request.form['birth_date']):
        flash("Invalid date format for birthdate -- must be yyyy-mm-dd.",'error')
    elif birth_date >= today:
        flash("Your birth date must be in the past.",'error')
    
    if len(email) < 1:
        flash("You must enter an email address.",'error')
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid email address.",'error')
    
    if len(password) < 1:
        flash("You must enter a password.",'error')
    elif len(password) < 9:
        flash("Passwords must be 9 characters or more.",'error')
    elif PASSWORD_REGEX.match(request.form['password']):
        flash("Passwords must contain at least uppercase letter and at least one number.",'error')
    
    if len(confirm_pwd) < 1:
        flash("You must confirm your password.",'error')
    elif confirm_pwd != password:
        flash("Confirm Password must match Password.",'error')
    
    return render_template('result.html', first_name=first_name, last_name=last_name, birth_date=birth_date,email=email, password=password, confirm_pwd=confirm_pwd) 

    # redirects back to the '/' route
    # return redirect('/')

app.run(debug=True) # run our server    