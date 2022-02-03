from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Main")
def authors(request):
    return HttpResponse("Authors")
def books(request):
    return HttpResponse("Books")
def authorDetails(request,authorId):
    return HttpResponse("Author details :"+str(authorId))
