from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("All hooked up inside Dojo_Ninja App")