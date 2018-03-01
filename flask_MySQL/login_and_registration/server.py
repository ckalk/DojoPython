from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
app.secret_key = 'KeepItSecretKeepItSafe'
mysql = MySQLConnector(app,'login_registration')

# the "md5" module will hash passwords
import md5

# the "re" module will let us perform some regular expression operations
import re
# Check for Valid Email format
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

# NAME_REGEX Check letters only, at least 2 characters /^[a-zA-Z]{2,}$/
NAME_REGEX = re.compile(r'^[a-zA-Z]{2,}$')

# PASSWORD_REGEX at least 8 characters /^.{8,}$/
PASSWORD_REGEX = re.compile(r'^.{8,}$')

@app.route('/') 
def index():
    return render_template('index.html')

@app.route('/validate_registration', methods=['POST'])
def validate_registration():
    errors = False
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    email = request.form['email']
    password = request.form['password']
    confirm_pwd = request.form['confirm_pwd']
    print first_name, last_name, email, password, confirm_pwd

#validate each field; add flash msg if fails validation
    if len(first_name) < 1:
        flash("You must enter your first name.",'regerror')
        errors = True
    elif not NAME_REGEX.match(request.form['first_name']):
        flash("Invalid characters or not at least 2 characters in first name.",'regerror')
        errors = True
    
    if len(last_name) < 1:
        flash("You must enter your last name.",'regerror')
        errors = True
    elif not NAME_REGEX.match(request.form['last_name']):
        flash("Invalid characters or not at least 2 characters in last name.",'regerror')
        errors = True
    
    if len(email) < 1:
        flash("You must enter an email address.",'regerror')
        errors = True
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid email address.",'regerror')
        errors = True
    
    if len(password) < 1:
        flash("You must enter a password.",'regerror')
        errors = True
    elif not PASSWORD_REGEX.match(request.form['password']):
        flash("Passwords must be 8 characters or more.",'regerror')
        errors = True
    
    if len(confirm_pwd) < 1:
        flash("You must confirm your password.",'regerror')
        errors = True
    elif confirm_pwd != password:
        flash("Confirm Password must match Password.",'regerror')
        errors = True
    
    if errors:
        # if errors, display them on index page
        return redirect('/')        
    else:
        # hash password md5
        hashed_password = md5.new(password).hexdigest()
        query = "INSERT INTO users ( first_name, last_name, email, password, created_at, updated_at) VALUES (:f_name, :l_name, :email, :h_password, NOW(), NOW() )"
        # Create a dictionary of data from POST.
        data = {
                'f_name': first_name,
                'l_name': last_name,
                'email': email,
                'h_password': hashed_password
                }
        # Run query, with dictionary values injected into the query.
        print 'Inserted registration'
        mysql.query_db(query, data)
        session['first_name'] = first_name
        session['last_name'] = last_name
        return redirect ('/success/registered')

@app.route('/validate_login', methods=['POST'])
def validate_login():
    errors = False
    email = request.form['email']
    password = request.form['password']

#validate login credentials
    if len(email) < 1 or len(password) < 1 :
        flash("You must enter your email and your password.",'loginerror')
        errors = True
        print 'email or password not entered -- login error detected'
    else:
        # hash entered password md5
        hashed_password = md5.new(password).hexdigest()
        query = "SELECT password, first_name, last_name FROM users WHERE email = '" + email + "'"
        print query
        # define your query
        result = mysql.query_db(query)
        print result
        # check to see if email was not found
        if len(result) < 1:
            flash("Email is not in registration database.",'loginerror')
            errors = True
            print 'email not found in db -- login error detected'
        #if email found, see if hashed password doesn't match what's in db
        elif result[0]['password'] <> hashed_password:
            flash("Password is not correct.",'loginerror')
            errors = True  
            print 'email found in db but incorrect pwd -- login error detected'
    print errors
    if errors:
        # if login errors, display them on index page
        return redirect('/')        
    else:
        # if no errors, display success page
        session['first_name'] = result[0]['first_name']
        session['last_name'] = result[0]['last_name']
        return redirect ('/success/loggedin')  

@app.route('/success/<action>')
def success(action):
    #if no errors, display success page
    flash("You are "+action+"!",'success')

    return render_template('success.html',first_name=session['first_name'], last_name=session['last_name']) 
        
app.run(debug=True) # run our server    