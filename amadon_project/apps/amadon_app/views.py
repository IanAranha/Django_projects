from django.shortcuts import render, HttpResponse, redirect
from . models import Item
from decimal import Decimal

this_session_total_charge=0.00

this_session_quantity=0

# Create your views here.
def index(request):
    request.session.flush()
    return redirect('/amadon')

def amadon(request):
    context={
        'items': Item.objects.all()
    }
    return render(request, 'index.html', context)

def buy(request):
    request.session['single_item_price']=Item.objects.single_item_price(request.POST)
    request.session['total_purchase_price']=Item.objects.total_price_calculator(request.POST)
    request.session['session_quantity']=Item.objects.this_session_quantity(request.POST)
    request.session['total_charges']=Item.objects.this_session_total()
    return redirect('/amadon/checkout')

def checkout(request):
    return render(request,'checkout.html')