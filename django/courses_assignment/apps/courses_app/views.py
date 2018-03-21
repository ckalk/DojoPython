from django.shortcuts import render, HttpResponse, redirect

# import object Class(es) from models.py
from .models import *

# import messages to use flask error messaging
from django.contrib import messages

# Inside your app's views.py file
from django.core.urlresolvers import reverse

def index(request):
    context = {
        "course_list": Course.objects.all()
        }
    return render(request, 'courses_app/index.html', context)


def create (request):
    print "in create route: request.POST = ", request.POST

    # Use validation performed in models.py
    errors = Course.objects.basic_validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect(reverse('courses:my_index')) # return to index page with errors
    else:
        name = request.POST['name']
        desc = request.POST['desc']
        course = Course.objects.create_course(name, desc)
        print "in create, added course with id =", course.id
        return redirect(reverse('courses:my_index')) # return to index page with no errors and show new course in listing


def delete(request, id):
    print "got to route to delete id ", id
    context = {
        "course": Course.objects.get(id=id)
        }
    return render(request, 'courses_app/delete.html', context)
    

def destroy(request, id):
    print "got to route to destroy id ", id
    c = Course.objects.get(id=id)
    c.delete()
    return redirect(reverse('courses:my_index'))
