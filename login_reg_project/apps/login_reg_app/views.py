from django.shortcuts import render, HttpResponse,redirect
from .models import User
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'login_reg_app/index.html')

def register(request):
    if request.method == 'POST':
        result = User.objects.userValidation(request.POST)
        if result['status'] == False:
            for error in result['errors']:
                messages.error(request, error, extra_tags='safe')
            return redirect('/')
        else:
            User.objects.userCreator(request.POST)
            messages.success(request, 'User has been registered. Please Log-in')  
            return redirect('/')
    else:
        return redirect('/')

def login(request):
    if request.method == 'POST':
        result=User.objects.loginValidation(request.POST)
        if result['status'] == False:
            for error in result['errors']:
                messages.error(request, error, extra_tags='safe')
            return redirect('/login')
        else:
            request.session['email'] = result['user'].email
            request.session['first_name'] = result['user'].first_name
            return redirect('/dashboard')
    else:
        return render(request, 'login_reg_app/login.html')

def dashboard(request):
    return render(request,'login_reg_app/dashboard.html')