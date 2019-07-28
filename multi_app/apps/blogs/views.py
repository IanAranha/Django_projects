from django.shortcuts import render,HttpResponse,redirect

# Create your views here.

def index(request):
    response = "place holder to display list of all blogs"
    return HttpResponse(response)

def new(request):
    response= "placeholder to display a new form to create a new blog" 
    return HttpResponse(response)

def create(request):
    return redirect('/blogs')

def show(request, num):
    return HttpResponse('placeholder to display blog {}'.format(num))

def edit(request, num):
    return HttpResponse('placeholder to edit blog {}'.format(num))

def destroy(request, num):
    return redirect('/blogs')