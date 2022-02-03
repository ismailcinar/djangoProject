from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Author

# Create your views here.

def index(request):
    return HttpResponse("Main")
def authors(request):
    template = loader.get_template('authors.html')
    context = {
        'authors_list' : Author.objects.all()
    }
    return render(request,'authors.html',context)
    #return HttpResponse(template.render(context,request))
def books(request):
    return HttpResponse("Books")
def authorDetails(request,authorId):
   #  template = loader.get_template('authorDetail.html')
     context = {
        'author_detail' : Author.objects.get(pk=authorId)
    } 
    return render(request,'authorDetail.html',context)