from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("All set from inside Book_Author_App")