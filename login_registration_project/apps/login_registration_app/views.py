from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'login_registration_app/index.html')

def register(request):
    if request.method == 'POST':
        result=User.objects.userValidation(request.POST)
        if result['status'] == True:
            user=User.objects.userCreater(request.POST)
            messages.success(request, 'User has been created. Please log-in')
        else:
            for error in result['errors']:
                messages.error(request, error)
    return redirect('/')

def login(request):
    if request.method == 'POST':
        result = User.objects.loginValidation(request.POST)
        if result['status'] == False:
           for error in result['errors']:
                messages.error(request, error)
                return redirect('/')
        request.session['email'] = result['user'].email
        request.session['first_name'] = result['user'].first_name
        return redirect('/dashboard')
        
def dashboard(request):
    return render(request, 'login_registration_app/success.html')