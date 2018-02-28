from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
app.secret_key = 'KeepItSecretKeepItSafe'
mysql = MySQLConnector(app,'friendships')

@app.route('/')
def index():
    # assuming want friends of user.id=1
    query = "SELECT friends.first_name AS friend_first_name, friends.last_name AS friend_last_name, friends.age AS friend_age, DATE_FORMAT(friendships.date_became_fr, '%b %D') AS mm_dd, YEAR(friendships.date_became_fr) AS yyyy FROM friendships LEFT JOIN users ON friendships.user_id = users.id LEFT JOIN users AS friends ON friends.id = friendships.friend_id WHERE friendships.user_id="+str(session['loggedin_id'])
    print query
    # define your query
    friends = mysql.query_db(query)           # run query with query_db()
    return render_template('index.html', all_friends=friends) # pass data to our template

@app.route('/login', methods=['POST'])
def get_user_id():
    # Write users info query as a string. Notice how we have multiple values
    query = "SELECT users.id FROM users WHERE users.first_name = '" + request.form["first_name"] + "' AND users.last_name = '" + request.form["last_name"] + "'"
    print query
    # SELECT returns a list of objects; get id from object in first element of list
    session['loggedin_id'] = mysql.query_db(query)[0]['id']
    print 'logged in id =', session['loggedin_id']
    return redirect('/')

@app.route('/friends', methods=['POST'])
def insert_friend():
    # Write users info query as a string. Notice how we have multiple values
    query = "INSERT INTO users ( first_name, last_name, age, created_at, updated_at) VALUES (:first_name, :last_name, :age, NOW(), NOW() )"
    # We'll then create a dictionary of data from the POST data received.
    data = {
            'first_name': request.form['first_name'],
            'last_name':  request.form['last_name'],
            'age': request.form['age'],
            }
    # Run query, with dictionary values injected into the query.
    #save the users.id of the inserted row in session variable
    print 'Inserted new friend'
    session['new_friend_id'] = mysql.query_db(query, data)
    print 'New friend id=', session['new_friend_id']

    # Now update friendships table with new friend id.
    query = "INSERT INTO friendships ( user_id, friend_id, date_became_fr, created_at, updated_at) VALUES (:user_id, :friend_id, DATE( NOW() ), NOW(), NOW() )"
    # We'll then create a dictionary of data from the POST data received.
    data = {
            'user_id': session['loggedin_id'],
            'friend_id':  session['new_friend_id']
            }
    # Run query, with dictionary values injected into the query.
    print 'Inserting new friend in friendships'
    mysql.query_db(query, data)
    print "new friendship added"
    return redirect('/')

app.run(debug=True)
