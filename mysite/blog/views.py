from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Post, user_profile
from django.http import HttpResponse
import datetime
def add_dob(request):
    request.user.date_of_birth=request.POST['add_dob']
def add_nickname(request):
    request.user.nickname=request.POST['nickname']
    return render(request, 'personal.html', {'user':request.user, 'all_blogs': all_blogs(), 'user_blogs': user_posts(request.user)})
def user_posts(user):
    return user.post_set.all().order_by('-created_on', '-updated_on')
def all_blogs():
    return Post.objects.all().order_by('-created_on', '-updated_on')
def homepage(request):
    return render(request,'homepage.html', {'all_blogs': all_blogs()})
def personal_homepage(request):
    return render(request, 'personal_homepage.html', {'user':request.user, 'all_blogs': all_blogs(), 'user_blogs': user_posts(request.user)})

def register(request):
    first_name=request.POST['first_name']
    last_name=request.POST['last_name']
    username=request.POST['username']
    password1=request.POST['password1']
    password2=request.POST['password2']
    emailid=request.POST['emailid']
    date_joined=datetime.datetime.now()
    if(password1==password2):
        if not (User.objects.all().filter(username=username).exists()):
            user=User.objects.create_user(username=username, password=password1, first_name=first_name, last_name=last_name, email=emailid)
            print ("user created")
            user.save()
            login(request, user)
            return render( request,'personal.html', {'user':user, 'all_blogs': all_blogs(), 'user_blogs': user_posts(user)})
        else:
            return render(request, 'blank.html')



def login_function(request):
    username=request.POST['username']
    print (username)
    password=request.POST['password']
    print (password)
    user=authenticate( request, username=username, password=password)
    if user is not None:
        print("valid")
        login(request, user)
        return render(request, 'personal.html',  {'user':user, 'all_blogs': all_blogs(), 'user_blogs': user_posts(user)})
    else:
        return render(request,'blank.html')


def add_blog(request):
    blog =request.user.post_set.create( title=request.POST['title'], content=request.POST['content'])
    blog.save()
    return render (request, 'personal.html',  {'user':request.user, 'all_blogs': all_blogs(), 'user_blogs': user_posts(request.user)})

def Logout(request):
    logout(request)
    return homepage(request)

def delete_post(request):
    titled=request.POST.get('blog_title')
    print(titled)
    Post.objects.all().get(title=titled).delete()
    return render (request, 'personal.html',  {'user':request.user, 'all_blogs': all_blogs(), 'user_blogs': user_posts(request.user)})


def edit_blog(request):
    titled=request.POST.get('old_title')
    if request.user.post_set.filter(title=titled).exists():

        blog=request.user.post_set.filter(title=titled)
        blog.title=request.POST['new_title']
        blog.content=request.POST['content']
        blog.save()
        return render(request, 'personal.html',  {'user':request.user, 'all_blogs': all_blogs(), 'user_blogs': user_posts(request.user)})
    else:
        return HttpResponse('<b>you dont have a blog with this title</b>')
def image_upload(request):
    request.user.profile_photo=request.POST.get('img')
    request.user.user_profile.save()
    return render (request, 'personal.html',  {'user':request.user, 'all_blogs': all_blogs(), 'user_blogs': user_posts(request.user)})
