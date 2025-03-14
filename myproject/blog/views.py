from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
def index(request):
    blog_title = "Latest Posts"
    posts = [
        {'id':1 ,'title': 'post 1', 'content': 'conent of post 1'},
        {'id':2 ,'title': 'post 2', 'content': 'conent of post 2'},
        {'id':3 ,'title': 'post 3', 'content': 'conent of post 3'},
        {'id':4 ,'title': 'post 4', 'content': 'conent of post 4'}
    ]
    return render(request, 'blog/index.html', {'title': blog_title, 'posts': posts})

def detail(request, post_id):
    return render(request, 'blog/detail.html', {'post_id': post_id})

def old_url_redirect(request):
    return redirect('blog:new_page_url')


def new_url(request):
    return HttpResponse("This is new URL")