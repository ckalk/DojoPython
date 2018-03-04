# Have 7 routes in your server.py
# Notice that for every form submission we use a POST method, while we're rendering our templates from get routes.

from flask import Flask, request, redirect, render_template, session, flash, get_flashed_messages, url_for
from mysqlconnection import MySQLConnector
app = Flask(__name__)
app.secret_key = 'KeepItSecretKeepItSafe'
mysql = MySQLConnector(app,'users')

import datetime
import time

# Define helper function to return user given if
def get_user_from_id(passed_id):
    query = "SELECT * FROM users WHERE id = :some_id"
    return mysql.query_db(query, {'some_id': passed_id})


# GET request to /users - calls the index method to display all the users. This will need a template.
@app.route('/users', methods=['GET'])
def index():

    title = "User's Show"

    # prepare flash messages info 
    flash_messages = get_flashed_messages(with_categories=True)
    staticfile = url_for('static', filename="users.css")

    userslist = []
    query = "SELECT id,CONCAT(first_name, ' ', last_name) AS full_name, email, DATE_FORMAT(created_at, '%M %D, %Y') AS created_date FROM users;"
    userslist = mysql.query_db(query)

    return render_template("users.html", 
            title = title,
            all_users = userslist, 
            messages = flash_messages, 
            styles = staticfile)


# GET /users/<id> - calls the show method to display the info for a particular user with given id. This will need a template.
@app.route('/users/<user_id>', methods=['GET'])
def show(user_id):

    title = "User's Show"

    # prepare flash messages info 
    flash_messages = get_flashed_messages(with_categories=True)
    staticfile = url_for('static', filename="users.css")

    query = "SELECT id,CONCAT(first_name, ' ', last_name) AS full_name, email, DATE_FORMAT(created_at, '%M %D, %Y') AS created_date FROM users WHERE id = :some_id ;"

    user = mysql.query_db( query, {'some_id':user_id} )

    return render_template("show_user.html", 
            title = title,
            user = user,
            messages = flash_messages, 
            styles = staticfile)


# POST /users/<id> - calls the update method to process the submitted form sent from /users/<id>/edit. Have this redirect to /users/<id> once updated.
@app.route('/users/<user_id>', methods=['POST'])
def update(user_id):

    errors = []
    first_name = request.form['f_name']
    last_name = request.form['l_name']
    email = request.form['email']

    #validate first name
    if len(first_name) < 1:
        errors.append("You must include your first name")

    #validate last name
    if len(last_name) < 1:
        errors.append("You must include your last name")

    #validate email
    if len(email) < 1:
        errors.append("You must include an email address")

    #Check that email (username) doesn't already exist in db
    query = "SELECT id FROM users WHERE email = :some_email AND id <> :some_id ;"
    data = { "some_email": email, "some_id":user_id } 
    # If true (not empty), then updated already in db for another user

    if mysql.query_db(query, data):
        errors.append("Email "+email+" already exists in database, so cannot be updated to that address")

    if errors: 
        #flash each error in list, then redirect 
        for e in errors: 
            flash(e, "error") 
        print "redirecting to edit route with user_id=", user_id
        return redirect("/users/"+user_id+"/edit")

    # else, update user if no errors 
    query = "UPDATE users SET first_name=:some_first_name, last_name=:some_last_name, email=:some_email, created_at=NOW(), updated_at=NOW() WHERE id = :some_id;"
    data = {
        "some_first_name": first_name,
        "some_last_name": last_name,
        "some_email": email,
        "some_id": user_id
        }
    mysql.query_db(query, data)

    # flash success message
    flash("Successfully updated user", "success")
    
    return redirect("/users/"+user_id)


# GET request /users/<id>/edit - calls the edit method to display a form allowing users to edit an existing user with the given id. This will need a template.
@app.route('/users/<user_id>/edit', methods=['GET'])
def edit(user_id):

    title = "Edit User "+user_id

    flash_messages = get_flashed_messages(with_categories=True)
    staticfile = url_for('static', filename="users.css") 

    query = "SELECT id,first_name, last_name, email FROM users WHERE id = :some_id ;"

    user = mysql.query_db( query, {'some_id':user_id} )

    return render_template("edit.html", 
            title = title,
            user = user,
            messages = flash_messages, 
            styles = staticfile)


# GET /users/<id>/destroy - calls the destroy method to remove a particular user with the given id. Have this redirect back to /users once deleted.
@app.route('/users/<user_id>/destroy', methods=['GET'])
def delete(user_id):

    query = "DELETE FROM users WHERE id = :some_id"
    mysql.query_db(query, {'some_id': user_id})

    # flash success message and return to dashboard page
    flash("Successfully deleted user", "success")

    return redirect("/users")


# GET request to /users/new - calls the new method to display a form allowing users to create a new user.
@app.route('/new', methods=['GET'])
def new():

    title = "User's New"

    flash_messages = get_flashed_messages(with_categories=True)
    staticfile = url_for('static', filename="users.css") 

    return render_template("new.html", 
            title = title,
            messages = flash_messages, 
            styles = staticfile)


# POST to /users/create - calls the create method to insert a new user record into our database. This POST should be sent from the form on the page /users/new. Have this redirect to /users/<id> once created.
@app.route('/users/create', methods=['POST'])
def create():

    errors = []
    first_name = request.form['f_name']
    last_name = request.form['l_name']
    email = request.form['email']

    #validate first name
    if len(first_name) < 1:
        errors.append("You must enter your first name")

    #validate last name
    if len(last_name) < 1:
        errors.append("You must enter your last name")

    #validate email
    if len(email) < 1:
        errors.append("You must enter an email address")

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
        return redirect("/new")
    
    # store new user if no errors 
    query = "INSERT INTO users (first_name, last_name, email, created_at, updated_at) VALUES (:some_first_name, :some_last_name, :some_email, NOW(), NOW() )"
    data = {
        "some_first_name": first_name,
        "some_last_name": last_name,
        "some_email": email
        }
    mysql.query_db(query, data)

    # flash success message and return to dashboard page
    flash("Successfully added user", "success")
    return redirect("/users")


app.run(debug=True) # run our server    