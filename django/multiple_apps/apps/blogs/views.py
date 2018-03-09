# / - display "placeholder to later display all the list of blogs" via HttpResponse. Have this be handled by a method named 'index'
# /new - display "placeholder to display a new form to create a new blog" via HttpResponse. Have this be handled by a method named 'new'
# /create - Have this be handled by a method named 'create'. For now, have this url redirect to /
# /{{number}} - display 'placeholder to display blog {{number}}'. For example /15 should display a message 'placeholder to display blog 15'.  Have this be handled by a method named 'show'
# /{{number}}/edit - display 'placeholder to edit blog {{number}}. Have this be handled by a method named 'edit'
# /{{number}}/delete - Have this be handled by a method named 'destroy'. For now, have this url redirect to /

from django.shortcuts import render, HttpResponse, redirect
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
        return redirect(index)
    else:
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