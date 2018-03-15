from django.shortcuts import render, HttpResponse, redirect
import random
import datetime 

now = datetime.datetime.now() 
today = now.strftime("%Y-%m-%d %I:%M %p")
print today

def index(request):
    if 'yourgold' not in request.session:
        request.session['yourgold'] = 0
        request.session['activities'] = []

    context = {
        "yourgold":request.session['yourgold'],
        "activities":request.session['activities']
    }

    return render(request, 'ninjagold/index.html', context)

def process_money(request, building):
    print request.session['yourgold']
    now = datetime.datetime.now() 
    today = now.strftime("%Y-%m-%d %I:%M %p")
    print today

    if building == 'farm':

        newgold = random.randint(10, 20)

        activity = {'msg':'Earned {} golds from the farm! ({})'.format(newgold, today), 'color':"green"}
        print activity

        request.session['activities'].insert(0,activity)

    elif building == 'cave':

        newgold = random.randint(5, 10)

        activity = {'msg': 'Earned {} golds from the cave! ({})'.format(newgold, today),'color':"green"}
        print activity

        request.session['activities'].insert(0,activity)

    elif building == 'house':

        newgold = random.randint(2, 5)

        activity = {'msg': 'Earned {} golds from the house! ({})'.format(newgold, today),'color':"green"}
        print activity

        request.session['activities'].insert(0,activity)

    else:
        newgold = random.randint(-50, 50)

        if newgold >= 0:
            activity = {'msg': 'Yay! You earned {} gold from the casino! ({})'.format(newgold, today),'color':"green"}

        else:
            activity = {'msg': 'Entered a casino and lost {} golds...Ouch... ({})'.format(newgold, today),'color':"red"}
        print activity

        request.session['activities'].insert(0,activity)

    request.session['yourgold'] = request.session['yourgold'] + newgold

    print newgold
    print request.session['yourgold']
    print request.session['activities']

    return redirect(index)

def reset(request):
    print "clearing request.session variables"
    request.session.clear()
    return redirect(index)