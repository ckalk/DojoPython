# / - display "placeholder to later display all the list of blogs" via HttpResponse. Have this be handled by a method named 'index'
# /new - display "placeholder to display a new form to create a new blog" via HttpResponse. Have this be handled by a method named 'new'
# /create - Have this be handled by a method named 'create'.  For now, have this url redirect to /
# /{{number}} - display 'placeholder to display blog {{number}}'.  For example /15 should display a message 'placeholder to display blog 15'.  Have this be handled by a method named 'show'
# /{{number}}/edit - display 'placeholder to edit blog {{number}}.  Have this be handled by a method named 'edit'
# /{{number}}/delete - Have this be handled by a method named 'destroy'. For now, have this url redirect to /

from django.shortcuts import render, HttpResponse, redirect
# the index function is called when root is visited
def index(request):
    response = "placeholder to later display all the list of blogs"
    return HttpResponse(response)
def new(request):
    response = "placeholder to display a new form to create a new blog"
    return HttpResponse(response)
def create(request):
    print "placeholder to create a new blog"
    return redirect(index)
def show(request, number):
    response = "placeholder to display blog "+number
    return HttpResponse(response)
def edit(request, number):
    response = "placeholder to edit blog "+number
    return HttpResponse(response)
def destroy(request, number):
    print "placeholder to destroy blog "+number
    return redirect(index)