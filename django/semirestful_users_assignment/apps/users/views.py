from django.shortcuts import render, HttpResponse, redirect

from django.contrib import messages

# import object Class(es) from models.py
from .models import User

# import messages to use flask error messaging
from django.contrib import messages

# a GET request to /users - calls the index method to display all the users. This will need a template.
def index(request):
    context = {
        "user_list": User.objects.all()
        }
    return render(request, 'users/index.html', context)

# GET request to /users/new - calls the new method to display a form allowing users to create a new user. This will need a template.
def new(request):

    return render(request, 'users/new.html')

#POST to /users/create - calls the create method to insert a new user record into our database. This POST should be sent from the form on the page /users/new. Have this redirect to /users/<id> once created.
def create(request):
    print "in create route: request.POST = ", request.POST

    # Use validation performed in models.py
    errors = User.objects.basic_validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
            return redirect('/users/new')

    else:
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        user = User.objects.create_user(fname, lname, email)
        print "in create, added user with id =", user.id
        return redirect('/users/'+str(user.id))


# GET /users/<id> - calls the show method to display the info for a particular user with given id. This will need a template.
def show(request, id):
    context = {
        "user": User.objects.get(id=id)
        }
    return render(request, 'users/show.html', context)


# GET request /users/<id>/edit - calls the edit method to display a form allowing users to edit an existing user with the given id. This will need a template.
def edit(request, id):
    context = {
        "user": User.objects.get(id=id)
        }
    return render(request, 'users/edit.html', context)


#POST /users/update - calls the update method to process the submitted form sent from /users/<id>/edit. Have this redirect to /users/<id> once updated.
def update(request, id):

    # Use validation and update performed in models.py

    errors = User.objects.update_validator(request.POST)
    print "in update route, returned from validator with errors=", errors
    # if errors in updated values found, return to /users/<id>/edit and display errors
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/users/'+id+'/edit')

    # if no errors in updated values found update was successful and show updated record
    else:
        return redirect('/users/'+id)


# GET /users/<id>/destroy - calls the destroy method to remove a particular user with the given id. Have this redirect back to /users once deleted.
def destroy(request, id):
    user_id = int(id)
    print "in destory with user_id=", user_id
    u = User.objects.get(id=user_id)
    u.delete()
    return redirect('/users')


# just added this in case I need it for testing purposes...
def reset(request):
    print "clearing session variables"
    request.session.clear()
    return redirect('/users')