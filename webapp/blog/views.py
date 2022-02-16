from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
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
  
class PostListView(ListView):
  model = Post
  template_name = 'blog/home.html'   #<app>/<model>_<viewtype>.html
  context_object_name = 'posts'
  ordering = ['-date_posted']

class PostDetailView(DetailView):
  model = Post
 
  

def about(request):
  #  return HttpResponse('<h1>Blog About</h1>')
    return render(request, 'blog/about.html',{'title':'About'})
