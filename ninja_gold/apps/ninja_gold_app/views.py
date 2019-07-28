from django.shortcuts import render, redirect
import random
from time import strftime, localtime

Total_Gold = 0
Temp_list = []
# Create your views here.
def index(request):
    global Temp_list
    request.session['gold'] = Total_Gold
    request.session['status'] = Temp_list
    context={
        'data' : request.session['status']
    }
    return render(request, "index.html", context)

def process_money(request):
    global Total_Gold
    global Temp_list
    wordtime = strftime('%H:%M:%S%p, %B %d %Y', localtime())
    if request.method == 'POST':
        if request.POST['building'] == 'farm':
            coin = random.randint(10,20)
            Total_Gold+=coin
            data={
                'status': 'You earned {} from the {}'.format(coin, request.POST['building']),
                'color': 'blue',
                'time' : wordtime,
            }
            Temp_list.append(data)
            request.session['status'] = Temp_list
            return redirect('/')
        elif request.POST['building'] == 'cave':
            coin = random.randint(5,10)
            Total_Gold+=coin
            data={
                'status': 'You earned {} from the {}'.format(coin, request.POST['building']),
                'color': 'blue',
                'time' : wordtime,
            }
            Temp_list.append(data)
            request.session['status'] = Temp_list
            return redirect('/')
        elif request.POST['building'] == 'house':
            coin = random.randint(2,5)
            Total_Gold+=coin
            data={
                'status': 'You earned {} from the {}'.format(coin, request.POST['building']),
                'color': 'blue',
                'time' : wordtime,
            }
            Temp_list.append(data)
            request.session['status'] = Temp_list
            return redirect('/')
        elif request.POST['building'] == 'casino':
            coin = random.randint(-50,50)
            Total_Gold+=coin
            if coin >= 0:
                data={
                'status': 'You earned {} from the {}'.format(coin, request.POST['building']),
                'color': 'blue',
                'time' : wordtime,
                }
                Temp_list.append(data)
                request.session['status'] = Temp_list
                return redirect('/')
            else:
                data={
                'status': 'You lost {} from the {}'.format(coin, request.POST['building']),
                'color': 'red',
                'time' : wordtime,
                }
                Temp_list.append(data)
                request.session['status'] = Temp_list
                return redirect('/')