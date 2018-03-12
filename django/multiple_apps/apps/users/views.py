from django.shortcuts import render, HttpResponse, redirect
# /register - display 'placeholder for users to create a new user record'
# /login - display 'placeholder for users to login' 
# /users/new - have the same method that handles /register also handle the url request of /users/new

# /users - display 'placeholder to later display all the list of users'
def index(request):
    response = "placeholder to later display all the list of users"
    return HttpResponse(response)

# /register - display 'placeholder for users to create a new user record'
def register(request):
    response = "placeholder for users to create a new user record"
    return HttpResponse(response)

# /login - display 'placeholder for users to login' 
def login(request):
    response = "placeholder for users to login"
    return HttpResponse(response)

# /users/new - have the same method that handles /register also handle the url request of /users/new
def new(request):
    response = "placeholder to display a new form to create a new blog"
    return redirect("/register")