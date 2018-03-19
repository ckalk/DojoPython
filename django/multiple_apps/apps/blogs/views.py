
from django.shortcuts import render, HttpResponse, redirect

from .models import Blog

# the index function is called when root is visited
# def index(request):
#     response = "placeholder to later display all the list of blogs"
#     return HttpResponse(response)
def index(request):
    context = {
        "email" : "blog@gmail.com",
        "name" : "cindy"
    }
    return render(request, "blogs/index.html", context)

# /new - display "placeholder to display a new form to create a new blog" via HttpResponse. Have this be handled by a method named 'new'
def new(request):
    response = "placeholder to display a new form to create a new blog"
    return HttpResponse(response)

# def create(request):
#     print "placeholder to create a new blog"
#     return redirect("/")
def create(request):
    if request.method == "POST":
        print "*"*50
        print request.POST
        print request.POST['name']
        print request.POST['desc']
        request.session['name'] = "test"
        print request.session['name']
        print "*"*50
        return redirect("/blogs")
    else:
        return redirect("/blogs")

# /{{number}} - display 'placeholder to display blog {{number}}'. For example /15 should display a message 'placeholder to display blog 15'.  Have this be handled by a method named 'show'
def show(request, number):
    response = "placeholder to display blog "+number
    return HttpResponse(response)

# /{{number}}/edit - display 'placeholder to edit blog {{number}}. Have this be handled by a method named 'edit'
def edit(request, number):
    response = "placeholder to edit blog "+number
    return HttpResponse(response)

# /{{number}}/delete - Have this be handled by a method named 'destroy'. For now, have this url redirect to /   
def destroy(request, number):
    print "placeholder to destroy blog "+number
    return redirect("/blogs")


# Use validation performed in models.py
def update(request):
    errors = Blog.objects.basic_validator(request.POST)
        if len(errors):
            for tag, error in errors.iteritems():
                messages.error(request, error, extra_tags=tag)
            return redirect('/blogs/edit/'+id)
        else:
            blog = Blog.objects.get(id = id)
            blog.name = request.POST['name']
            blog.desc = request.POST['desc']
            blog.save()
            return redirect('/blogs')