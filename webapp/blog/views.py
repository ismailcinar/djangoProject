from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
# posts = [
#     {
#         'author' : 'İsmailÇ',
#         'title' : 'Blog Post',
#         'content' : 'First post content',
#         'date_posted' : 'November 11, 1998',
#     },
#       {
#         'author' : 'KazımK',
#         'title' : 'Blog Post 2',
#         'content' : 'Second post content',
#         'date_posted' : 'December 11, 1998',
#     }
# posts:posts]


def home(request):
   # return HttpResponse('<h1>Blog Home</h1>')
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html',context)
def about(request):
  #  return HttpResponse('<h1>Blog About</h1>')
    return render(request, 'blog/about.html',{'title':'About'})
