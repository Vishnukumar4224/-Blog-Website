import logging
from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from .models import post
# Create your views here.

# Static demo data
# posts = [
#         {'id':1 ,'title': 'post 1', 'content': 'content of post 1'},
#         {'id':2 ,'title': 'post 2', 'content': 'content of post 2'},
#         {'id':3 ,'title': 'post 3', 'content': 'content of post 3'},
#         {'id':4 ,'title': 'post 4', 'content': 'content of post 4'}
#     ]

def index(request):
    blog_title = "Latest Posts"
    posts = post.objects.all()
    return render(request, 'blog/index.html', {'title': blog_title, 'posts': posts})

def detail(request, slug):

    # static demo data
    # post = next((item for item in posts if item['id'] == int(post_id)), None) # this get the perticular posts items if not it write None

    # getting data from model by id..pk->primary key
    try:
        Post = post.objects.get(slug=slug)
    except post.DoesNotExist:
        raise Http404("Post does not exist")
    

    # logger = logging.getLogger("TESTING")
    # logger.debug(f'post variable is {post}')

    return render(request, 'blog/detail.html', {'post': Post})

def old_url_redirect(request):
    return redirect('blog:new_page_url')


def new_url(request):
    return HttpResponse("This is new URL")