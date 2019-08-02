from django.shortcuts import render, HttpResponse,redirect
from .models import User
from django.contrib import messages

# Create your views here.
def index(request):
    return redirect('/users')

def show_all(request):
    context={
        'users': User.objects.all(),
    }
    return render(request, 'index.html', context)

def new(request):
    return render(request, 'new.html')

def create(request):
    errors=User.objects.basicValidator(request.POST)
    if len(errors):
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/users/new')
    else:
        User.objects.create(
            first_name=request.POST['first_name'],
            last_name=request.POST['last_name'],
            email=request.POST['email'],
        )
        messages.success(request, "User successfully created")
        return redirect('/users')

def show_one(request, id):
    if request.method == 'POST':
        u=User.objects.get(id=id)
        u.first_name = request.POST['first_name']
        u.last_name = request.POST['last_name']
        u.email = request.POST['email']
        u.save()   
    context={
        'user': User.objects.get(id=id)
    }
    return render(request, 'show.html', context)

def edit(request, id):
    context={
        'user': User.objects.get(id=id)
    }
    return render(request, 'edit.html', context)

def destroy(request, id):
    User.objects.get(id=id).delete()
    return redirect('/users')