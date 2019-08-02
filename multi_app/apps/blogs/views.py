from django.shortcuts import render,HttpResponse,redirect
from django.contrib import messages
# Create your views here.

from models import Blog
        
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

def update(request, id):
    errors=Blog.objects.basicValidator(request.POST)
    if len(errors):
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/blog/edit/'+id)
    else:
        blog = Blog.objects.get(id = id)
        blog.name = request.POST['name']
        blog.desc = request.POST['desc']
        blog.save()
        messages.success(request, "Blog successfully updated")
        return redirect('/blogs')

def destroy(request, num):
    return redirect('/blogs')