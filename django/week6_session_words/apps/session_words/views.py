from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime

def index(request):
    #initialize session dictionary list to hold words
    if 'words' not in request.session:
        print "initializing request.session('words')"
        request.session['words'] = []
    return render(request, "session_words/index.html")

def add_word(request):
    print 'Adding a word'
    word = request.POST['word']
    color = request.POST['color']
    word_added = datetime.strftime(datetime.now(), "%H:%M:%S %p, %B %d %Y")
    
    # see if checkbox named font_sz was checked
    # print "request.POST=", request.POST
    if "font_sz" in request.POST:
        font_sz = "bigger"
    else: 
        font_sz = "normal"

    #append dictionary to session list that holds words
    # Session object not directly modified, only data within the session. Session changes not saved!
    request.session["words"].append({'word': word, 'color':color, 'font':font_sz, 'date':word_added})

    # Set session as modified to force data updates to be saved.
    request.session.modified = True

    return redirect(index)

def clear(request):
    request.session.clear()
    return redirect(index)
