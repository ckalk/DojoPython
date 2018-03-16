from django.shortcuts import render, HttpResponse, redirect

def index(request):

    return render(request, 'dojo_ninjas/index.html')