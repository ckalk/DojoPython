from django.shortcuts import render, HttpResponse, redirect

# import object Class(es) from models.py
from .models import *

# import messages to use flask error messaging
from django.contrib import messages

# Inside your app's views.py file
from django.core.urlresolvers import reverse

def index(request):

    return render(request, 'users/index.html')


def register (request):
    print "***** in register route: request.POST = ", request.POST

    # Use validation performed in models.py
    errors = User.objects.reg_validator(request.POST)

    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
         # return to index page with errors

        # figure out what is stored in messages...
       
        print "type of messages = ", type(messages)

        for dic in messages:
            for key in dic:
                print dic[key]

        return redirect(reverse('users:my_index')) 

    else:
        new_user = User.objects.create_user(request.POST)
        request.session['id'] = new_user.id
        messages.success(request, "Thank you {} {} for registering".format(new_user.first_name, new_user.last_name))
        return redirect(reverse('users:my_success')) 


def login (request):
    print "***** in login route: request.POST = ", request.POST

    # Use validation performed in models.py
    errors = User.objects.login_validator(request.POST)

    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        # return to index page with errors
        return redirect(reverse('users:my_index')) 

    else:
        user = User.objects.get(email=request.POST["email"])
        request.session['id'] = user.id
        messages.success(request, "Thank you {} {} for logging in".format(user.first_name, user.last_name))
        return redirect(reverse('users:my_success')) 


def success(request):
    context = {
        "user": User.objects.get(id=request.session['id'])
    }
    return render(request, 'users/success.html', context)