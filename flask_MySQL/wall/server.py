from flask import Flask, request, redirect, render_template, session, flash, get_flashed_messages, url_for
from mysqlconnection import MySQLConnector
app = Flask(__name__)
app.secret_key = 'KeepItSecretKeepItSafe'
mysql = MySQLConnector(app,'wall')

import datetime
import time

# the "md5" module will hash passwords
import md5
# but the Bcrypt hashing module seems better
from flask_bcrypt import Bcrypt
bc = Bcrypt(app)


# the "re" module will let us perform some regular expression operations
import re
# Check for Valid Email format
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
# NAME_REGEX Check letters only, at least 2 characters /^[a-zA-Z]{2,}$/
NAME_REGEX = re.compile(r'^[a-zA-Z]{2,}$')
# PASSWORD_REGEX at least 8 characters /^.{8,}$/
PASSWORD_REGEX = re.compile(r'^.{8,}$')


# Define helper function to return user given if
def get_user_from_id(passed_id):
    query = "SELECT * FROM users WHERE id = :some_id"
    return mysql.query_db(query, {'some_id': passed_id})


@app.route('/') 
def index():
    flash_messages = get_flashed_messages(with_categories=True)
    staticfile = url_for('static', filename="wall.css")
    return render_template("index.html", 
            messages = flash_messages, 
            styles = staticfile)


@app.route('/register', methods=['POST'])
def register():

    errors = []
    first_name = request.form['f_name']
    last_name = request.form['l_name']
    email = request.form['email']
    password = request.form['password']
    confirm_pwd = request.form['confirm_password']

    #validate first name
    if len(first_name) < 1:
        errors.append("You must enter your first name")
    elif not NAME_REGEX.match(first_name):
        errors.append("Invalid characters or not at least 2 characters in first name")

    #validate last name
    if len(last_name) < 1:
        errors.append("You must enter your last name")
    elif not NAME_REGEX.match(last_name):
        errors.append("Invalid characters or not at least 2 characters in last name") 

    #validate email
    if len(email) < 1:
        errors.append("You must enter an email address")
    elif not EMAIL_REGEX.match(request.form['email']):
        errors.append("Invalid email address") 

    #validate password
    if len(password) < 1:
        errors.append("You must enter a password")
    elif not PASSWORD_REGEX.match(request.form['password']):
         errors.append("Passwords must be 8 characters or more")

    #validate confirm_password
    if len(confirm_pwd) < 1:
        errors.append("You must confirm password")
    elif confirm_pwd != password:
        errors.append("Password and Confirm Password must match")

    #Check that email (username) doesn't already exist in db
    query = "SELECT id FROM users WHERE email = :some_email"
    data = { "some_email": email}
    # If true (not empty), then user already in db
    if mysql.query_db(query, data):
        errors.append("Email address already exists in database")

    if errors: 
        #flash each error in list, then redirect 
        for e in errors: 
            flash(e, "error") 
        return redirect("/")

    # create a user if no errors 
    hashed_pw = bc.generate_password_hash(password)
    query = "INSERT INTO users (first_name, last_name, email, password, created_at, updated_at)\
        VALUES (:some_fname, :some_lname, :some_email, :some_password, NOW(), NOW() )"
    data = {
        "some_fname": first_name,
        "some_lname": last_name, 
        "some_email": email,
        "some_password": hashed_pw
    }
    mysql.query_db(query, data)
    flash("Successfully Registered", "success")

    return redirect("/")


@app.route('/login', methods=['POST'])
def login():

    errors = []

    # does username exist? 
    query = "SELECT password, id FROM users WHERE email = :some_email" 
    data = { 
    "some_email": request.form['email'] 
    }

    wall_user = mysql.query_db(query, data)
    # if this list is empty, that username is not registered
    if not wall_user: 
        errors.append("Invalid email/password") 
    # else is registered , so check for password match
    else: 
        # use bcrypt to compare password hashes
        # this bcrypt function checks if stored hash matches form password (if hashed)
        if not bc.check_password_hash(wall_user[0]['password'], request.form['password']):
            errors.append("Invalid email/password") 
    
    if errors: 
        #flash each error in list, then redirect 
        for e in errors: 
            flash(e, "error") 
        return redirect("/")

    # store user's id to session  and go to success page
    session['id'] = wall_user[0]['id']
    flash("Successfully Logged In!", "success")
    print "user logged in with id = ", session['id']
    return redirect("/dashboard")


# LOGIN PROTECTED AREA
@app.route('/dashboard')
def dashboard():
    # test to see that user is logged in
    try:
        test_user = get_user_from_id(session['id'])
    except KeyError:
        return redirect("/")

    # logged in, so prepare header and flash messages info 
    flash_messages = get_flashed_messages(with_categories=True)
    staticfile = url_for('static', filename="wall.css")
    full_name = test_user[0]["first_name"]+" "+test_user[0]["last_name"]

    #get list of existing posts, ordered by most recent first
    postslist = []
    query = "SELECT messages.id, messages.user_id, messages.message,CONCAT(users.first_name, ' ', users.last_name) AS full_name,  DATE_FORMAT(messages.created_at, '%M %D %Y') AS post_date FROM messages JOIN users ON users.id = messages.user_id ORDER BY messages.created_at DESC;"

    postslist = mysql.query_db(query)

    for post in postslist:
        msg_id = post["id"]
        cmntslist = []

        query = "SELECT comments.user_id, comments.comment AS comment, CONCAT(users.first_name, ' ', users.last_name) AS comment_name, DATE_FORMAT(comments.created_at, '%m %b %Y') AS comment_date FROM comments JOIN users ON users.id = comments.user_id WHERE comments.message_id = :some_id ORDER BY comments.created_at ASC;"
        cmntslist = mysql.query_db(query, {'some_id': msg_id})

        # create a dict in post to hold the list of comments
        post["comments"] = cmntslist

    return render_template("dashboard.html", 
            name = full_name, 
            posts = postslist,
            messages = flash_messages, 
            styles = staticfile)


@app.route('/postmsg', methods=['POST'])
def post_message():
    # test to see that user is logged in
    try:
        test_user = get_user_from_id(session['id'])
    except KeyError:
        return redirect("/")

    errors = []
    flash_messages = []

    # Check that post is not empty
    content = request.form["post-content"]
    if len(content) < 1:
        errors.append("Your post is empty")

    if errors: 
        #flash each error in list, then redirect 
        for e in errors: 
            flash(e, "error") 
        return redirect("/dashboard")

    # store post if no errors 
    query = "INSERT INTO messages (user_id, message, created_at, updated_at)\
        VALUES (:some_id, :some_message, NOW(), NOW() )"
    data = {
        "some_id": session["id"],
        "some_message": content
    }
    mysql.query_db(query, data)

    # flash success message and return to dashboard page
    flash("Successfully added your post", "success")
    return redirect("/dashboard")


@app.route('/postcmnt/<msg_id>', methods=['POST'])
def post_comment(msg_id):
    # test to see that user is logged in
    try:
        test_user = get_user_from_id(session['id'])
    except KeyError:
        return redirect("/")

    errors = []
    flash_messages = []

    # Check that comment is not empty
    content = request.form["cmnt-content"]
    if len(content) < 1:
        errors.append("Your comment is empty")

    if errors: 
        #flash each error in list, then redirect 
        for e in errors: 
            flash(e, "error") 
        return redirect("/dashboard")

    # store comment if no errors 
    query = "INSERT INTO comments (message_id, user_id, comment, created_at, updated_at)\
        VALUES (:some_message_id, :some_user_id, :some_comment, NOW(), NOW() )"
    data = {
        "some_message_id": msg_id,
        "some_user_id": session["id"],
        "some_comment": content
    }
    mysql.query_db(query, data)

    # flash success message and return to dashboard page
    flash("Successfully added your comment", "success")
    return redirect("/dashboard")


@app.route('/deletepost/<msg_id>')
def delete_post(msg_id):

    # test to see that user is logged in
    try:
        test_user = get_user_from_id(session['id'])
    except KeyError:
        return redirect("/")

    # Do time calculation so can check if post was made within last 30 minutes
    query = "SELECT created_at FROM messages WHERE id = :some_id"
    post_date =  mysql.query_db(query, {'some_id': msg_id})
    NOW = datetime.datetime.now()

    # Convert to Unix timestamp
    d1_ts = time.mktime(NOW.timetuple())
    d2_ts = time.mktime(post_date[0]["created_at"].timetuple())
    # They are now in seconds, subtract and then divide by 60 to get minutes.
    elapsed = int(d1_ts - d2_ts) / 60

    if elapsed > 30:
        # flash error message and return to dashboard page
        flash("Post is older than 30 minutes and so cannot be deleted", "error")
        return redirect("/dashboard")

    # Delete post and all of its comments
    # Note: since comments.message_id (foreign key) is set to ON DELETE = Cascade, comments related to the post will be automatically deleted

    query = "DELETE FROM messages WHERE id = :some_id"
    mysql.query_db(query, {'some_id': msg_id})

    # flash success message and return to dashboard page
    flash("Successfully deleted your post", "success")
    return redirect("/dashboard")


@app.route('/logout')
def logout():
    session.clear()
    print 'logged out'
    return redirect("/")


app.run(debug=True) # run our server    