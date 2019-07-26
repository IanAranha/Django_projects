from django.shortcuts import render,HttpResponse,redirect

# Create your views here.

def index(request):
    response = "THIS IS A response!"
    return HttpResponse(response)