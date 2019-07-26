from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime
from django.utils.crypto import get_random_string

# Create your views here.
def index(request):
    print('HELLO')
    print(strftime("%Y-%m-%d    %H:%M" , gmtime()))
    context ={
        'email' : 'blog@email.com',
        'name': "Ian"
    }
    return render(request,'blogs/index.html',context)

def new(request):
    return HttpResponse('placeholder to display a new form to create a new blog')

def create(request):
    if request.method == 'POST':
        print("*" * 50)
        print(request.method)
        print(request.POST['title'])
        print(request.POST['description'])
        request.session['name'] = request.POST['title']
        return redirect('/')
    else:
        return redirect('/')

def show(request, num):
    return HttpResponse('placeholder to display blog {}'.format(num))

def edit(request, num):
    return HttpResponse('placeholder to edit blog {}'.format(num))

def destroy(request, num):
    return redirect('/')