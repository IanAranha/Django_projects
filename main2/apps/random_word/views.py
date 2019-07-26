from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string




# Create your views here.
COUNT = 0

def index(request):
    r=get_random_string(length=15)
    global COUNT
    COUNT += 1
    Context={
        'word': r.upper(),
        'count': COUNT
    }
    return render (request, 'index.html', Context)