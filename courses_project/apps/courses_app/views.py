from django.shortcuts import render, redirect
from .models import Course
from django.contrib import messages

# Create your views here.
def index(request):
    context={
        'courses' : Course.objects.all()
    }
    return render(request,'index.html', context)

def add_course(request):
    if request.method =='POST':
        errors=Course.objects.basicValidator(request.POST)
        if len(errors):
            for value in errors.items():
                messages.error(request, value)
            return redirect('/index')
        else:
            Course.objects.create(
                name=request.POST['name'],
                desc=request.POST['desc']
            )
            messages.success(request,'Course has been added')
            return redirect('/')

def destroy(request, id):
    context={
        'course': Course.objects.get(id=id)
    }
    return render(request, 'destroy.html', context)

def delete(request, id):
    Course.objects.get(id=id).delete()
    return redirect('/')