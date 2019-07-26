from django.shortcuts import render, HttpResponse, redirect

count = 0
# Create your views here.
def index(request):
    global count
    data={
        'count': count
    }
    return render(request, 'index.html', data)

def process(request):
    global count
    if request.method == "POST":
        count+=1
        request.session['count'] = count
        request.session['name'] = request.POST['name']
        request.session['location'] = request.POST['location']
        request.session['language'] = request.POST['language']
        request.session['comment'] = request.POST['comment']
        return redirect('/result')
    else:
        return redirect('/')

def result(request):
    data={
        'count': request.session['count'],
        'counter' : request.session['count'],
        'name' : request.session['name'],
        'location': request.session['location'],
        'language': request.session['language'],
        'comment': request.session['comment']
    }
    return render(request, 'result.html', data)