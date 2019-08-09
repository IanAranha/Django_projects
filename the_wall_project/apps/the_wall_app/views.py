from django.shortcuts import render, redirect
from .models import User, Message, Comment
from django.contrib import messages

# Create your views here.
def index(request):
    request.session.flush()
    return render(request, 'the_wall_app/index.html')

def register(request):
    if request.method == 'POST':
        result = User.objects.userValidation(request.POST)
        if result['status'] == False:
            for error in result['errors']:
                messages.error(request, error, extra_tags='safe')
            return redirect('/')
        else:
            User.objects.userCreator(request.POST)
            messages.success(request, "User has been registered. Please log in")  
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
            request.session['id'] = result['user'].id
            return redirect('/dashboard')
    else:
        return render(request, 'the_wall_app/login.html')

def dashboard(request):
    if 'email' not in request.session:
        return redirect('/')
    else:
        all_messages=Message.objects.all().order_by('-created_at')
        all_comments=Comment.objects.all().order_by('-created_at')
        return render(request,'the_wall_app/dashboard.html', {
                    'posted_messages' : all_messages,
                    'posted_comments' : all_comments,
                })

def postMessage(request):
    result=Message.objects.postMessage(request.POST)
    if result['status'] == False:
        messages.error(request, "Please enter some text!", extra_tags='safe')
        return redirect('/dashboard')
    else:
        Message.objects.messageCreator(request.POST)
        return redirect('/dashboard')

def postComment(request):
    result=Comment.objects.postComment(request.POST)
    if result['status'] == False:
        messages.error(request, "Please enter some text!", extra_tags='safe')
        return redirect('/dashboard')
    else:
        Comment.objects.create(
            comment=request.POST['comment'],
            user=User.objects.get(id=request.session['id']),
            message=Message.objects.get(id=request.POST['message_id']) )
        return redirect('/dashboard')

def delete(request, id):
    Message.objects.deleteMessage(id)
    return redirect('/dashboard')


def logout(request):
    request.session.flush()
    return redirect('/')