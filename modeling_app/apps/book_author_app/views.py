from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("All hooked up from inside the book_author_app")