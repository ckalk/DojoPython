from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string

# the index function is called when root is visited
def index(request):
    print "*** called random_word index page"

    if 'counter' not in request.session:
        request.session['counter'] = 0

    context = {
        "word" : get_random_string(length=14, allowed_chars='ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    }

    return render(request, "random_word/index.html", context)

def new(request):
    request.session['counter']+=1
    return redirect(index)

def reset(request):
    request.session['counter']=0
    return redirect(index)
