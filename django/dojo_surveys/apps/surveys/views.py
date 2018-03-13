from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
# the index function is called when root is visited

def index(request):
    return render(request, "surveys/index.html")

def process(request):
    if request.method == "POST":
        print "Got POST Info"
        print request.POST['name']
        print request.POST['location']
        print request.POST['fav_language']
        print request.POST['comment']

    #validate that the name field is not empty 
        if len(request.POST['name']) < 1:
            messages.add_message(request, messages.ERROR, 'Name field cannot be empty!')
        else:
            msg_str="Success! Your name field is {}.".format(request.POST['name'])
            print msg_str
            messages.add_message(request, messages.SUCCESS, msg_str )
    #validate that the comment field is not empty   
        if len(request.POST['comment']) < 1:
            messages.add_message(request, messages.ERROR, 'Comment field cannot be empty!')
    # validate that the comment field is no longer than 120 characters
        elif len(request.POST['comment']) > 120:
           messages.add_message(request, messages.ERROR, 'Comment field cannot be longer than 120 characters.')
        else:
            msg_str = "Success! Your comment field ({}) is less than 120 characters.".format(request.POST['comment'])
            print msg_str
            messages.add_message(request, messages.SUCCESS, msg_str)
     
        request.session['name'] = request.POST['name']
        request.session['location'] = request.POST['location']
        request.session['fav_language']= request.POST['fav_language']
        request.session['comment'] = request.POST['comment']     
    return redirect(result)

def result(request):
    context = {
        "result_name" : request.session['name'],
        "result_loc" : request.session['location'],
        "result_lang" : request.session['fav_language'],
        "result_cmnt" : request.session['comment']     
    }
    print "context=", context
    return render(request, "surveys/result.html", context) 

