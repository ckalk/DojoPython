''' Assignment: Disappearing Ninja
Build a flask application with the below functionality.
This exercise will help you practice URL routing, using views, and rendering static content.
These are the routes that you need to set up:
    On the default page ('localhost:5000'), it should display a view that says "No ninjas here"
    When user visits /ninja, it should display all four Ninja Turtles (Leonardo, Michelangelo, Raphael, and Donatello)
    /ninja/[ninja_color], should display the corresponding Ninja Turtle (grab the color parameter out of the requested URL). If:
    * /ninja/blue, it should only display the Ninja Turtle Leonardo.
    * /ninja/orange - Ninja Turtle Michelangelo.
    * /ninja/red - Ninja Turtle Raphael
    * /ninja/purple - Ninja Turtle Donatello
    * other than the colors (Blue, Orange, Red, and Purple), example: /ninja/black or /ninja/123, then display the image notapril.jpg
    You'll need to remember how to use static files for this assignment. '''

from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/') 
def index():
    print "display index page"
    return render_template('index.html')

@app.route('/ninja/<color>')
def display_ninja(color):
    print "display ninja page"
    print color
    return render_template("ninja.html", color=color)

app.run(debug=True) # run our server    