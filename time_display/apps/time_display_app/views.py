from django.shortcuts import render
from datetime import datetime
from time import gmtime, strftime

# Create your views here.
def index(request):
    now = datetime.now()
    
    data={
        'date': now,
        "time": strftime("%H:%M:%S %p", gmtime())
    }

    return render (request , 'index.html', data)