import logging
from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.

posts = [
        {'id':1 ,'title': 'post 1', 'content': 'content of post 1'},
        {'id':2 ,'title': 'post 2', 'content': 'content of post 2'},
        {'id':3 ,'title': 'post 3', 'content': 'content of post 3'},
        {'id':4 ,'title': 'post 4', 'content': 'content of post 4'}
    ]

def index(request):
    blog_title = "Latest Posts"

    return render(request, 'blog/index.html', {'title': blog_title, 'posts': posts})

def detail(request, post_id):
    post = next((item for item in posts if item['id'] == int(post_id)), None) # this get the perticular posts items if not it write None

    # logger = logging.getLogger("TESTING")
    # logger.debug(f'post variable is {post}')

    return render(request, 'blog/detail.html', {'post': post})

def old_url_redirect(request):
    return redirect('blog:new_page_url')


def new_url(request):
    return HttpResponse("This is new URL")