from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    return HttpResponse('placeholder to later display all the list of blogs')

def new(request):
    return HttpResponse('placeholder to display a new form to create a new blog')

def create(request):
    return redirect('/')

def show(request, num):
    return HttpResponse('placeholder to display blog {}'.format(num))

def edit(request, num):
    return HttpResponse('placeholder to edit blog {}'.format(num))

def destroy(request, num):
    return redirect('/')