import logging
from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from .models import post, about_us
from django.core.paginator import Paginator
from .forms import ContactForm, RegisterForm

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

    #getting data from post model
    posts = post.objects.all()

    #pagination
    paginator = Paginator(posts, 5)
    page_number = request.GET.get('page')
    page_object = paginator.get_page(page_number)
    


    return render(request, 'blog/index.html', {'title': blog_title, 'posts': page_object})

def detail(request, slug):

    # static demo data
    # post = next((item for item in posts if item['id'] == int(post_id)), None) # this get the perticular posts items if not it write None

    # getting data from model by id..pk->primary key
    try:
        Post = post.objects.get(slug=slug)
        related_post = post.objects.filter(category = Post.category).exclude(pk=Post.pk)

    except post.DoesNotExist:
        raise Http404("Post does not exist")
    

    # logger = logging.getLogger("TESTING")
    # logger.debug(f'post variable is {post}')

    return render(request, 'blog/detail.html', {'post': Post, 'related_posts': related_post})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        logger = logging.getLogger("TESTING")
        if form.is_valid():
            logger.debug(f'POST Data is {form.cleaned_data['name']} {form.cleaned_data['email']} {form.cleaned_data['message']}')
            #send email or save in database
            success_message = 'Your Email has been sent!'
            return render(request,'blog/contact.html', {'form':form,'success_message':success_message})
        else:
            logger.debug('Form validation failure')
        return render(request,'blog/contact.html', {'form':form, 'name': name, 'email':email, 'message': message})
    return render(request,'blog/contact.html')

def about(request):
    about_content = about_us.objects.first()
    if about_content == None or not about_content.content:
        about_content = "About us content is not available" #Default content
    else:
        about_content = about_content.content
    return render(request, 'blog/about.html', {'content': about_content })



def register(request):
    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False) #user data created
            user.set_password(form.cleaned_data['password']) #password encrypted
            user.save()
            print('User created')

    return render(request, 'blog/register.html', {'form': form})



# def old_url_redirect(request):
#     return redirect('blog:new_page_url')


# def new_url(request):
#     return HttpResponse("This is new URL")