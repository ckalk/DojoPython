from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
app.secret_key = 'KeepItSecretKeepItSafe'
mysql = MySQLConnector(app,'email_validation')

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

@app.route('/') 
def index():
    return render_template('index.html')

@app.route('/success', methods=['POST'])
def validate():
    errors = False
    email = request.form['email']
    print  email
#validate email; add flash msg if fails validation
    if len(email) < 1:
        flash("You must enter an email address.",'error')
        errors = True
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Email is not valid!",'error')
        errors = True

    if errors:
        # if errors, display them on index page
        return redirect('/')        
    else:
        #if no errors, display success page
        new_email=request.form['email']
        flash("The email address you entered ("+ new_email + ") is a VALID email address! Thank you!",'success')
        # Write users info query as a string. Notice how we have multiple values

        query = "INSERT INTO users ( email, created_at, updated_at) VALUES (:email, NOW(), NOW() )"
        # Create a dictionary of data from POST.
        data = {
                'email': new_email
                }
        # Run query, with dictionary values injected into the query.
        print 'Inserted email'
        mysql.query_db(query, data)

        # Now pull all emails from db to send to success page
        query = "SELECT email, DATE_FORMAT(created_at, '%m/%e/%y @ %h:%i %p') AS date_created FROM users"
        emails = mysql.query_db(query) 
        print emails
        # pass returned data to our template
        return render_template('success.html', list_of_emails=emails)
        
app.run(debug=True) # run our server    