from django.shortcuts import render, HttpResponse, redirect
from time import strftime, localtime
temp_list=[]
# Create your views here.
def index(request):
    request.session.clear()
    return render(request, 'index.html')

def addWordToSession(request):
    if request.method == 'POST':
        wordtime = strftime('%H:%M:%S%p, %B %d %Y', localtime())
        if 'font' in request.POST:
            data = {
                'word': request.POST['word'],
                'color': request.POST['color'],
                'font': 'big',
                'time': wordtime
            }
        else:
            data = {
                'word': request.POST['word'],
			    'color': request.POST['color'],
			    'font': 'small',
			    'time': wordtime
            }
        temp_list.append(data)
        request.session['word'] = temp_list
        return redirect('/show')

def show(request):
    context={
        'data' : request.session['word']
    }
    return render(request,'index.html', context)