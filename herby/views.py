from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from .models import Post
from django.shortcuts import render 
from django.utils import timezone
from .forms import  CommentForm
from django.contrib import auth

from .models import Post

# Create your views here.

def start(request):
    return render(request, 'start.html')

def main(request):
    posts = Post.objects
    return render(request, 'main.html' , {'posts':posts})

def detail(request, post_id):
    post_detail = get_object_or_404(Post, pk=post_id)
    return render(request, 'detail.html', {'post':post_detail})

def search(request):
    return render(request, 'search.html')

def accounts(request):
    return render(request, 'base.html')

def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
            auth.login(request, user)
            return redirect('main')
    return render(request, 'signup.html')

def signin(request):
    if request.method =="POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('main')
        else:
            return render(request, 'signin.html', {'error' : '로그인에 실패하셨습니다. 아이디와 비밀번호를 확인해주세요'})

    return render(request, 'signin.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('signin')
    return render(request, 'signin.html')     

def new(request):
    return render(request, 'openclass.html') 

def create(request):
    post = Post()
    post.title = request.GET['title']
    post.body = request.GET['body']
    post.myuni = request.GET['myuni']
    post.pub_date = timezone.datetime.now()
    post.save()
    return redirect('/herby/' + str(post.id))

def delete(request, post_id):
    post=Post.objects.get(pk=post_id)
    post.delete()
    return redirect('main')

def add_comment(request, post_id):
    post = get_object_or_404(Post, pk = post_id)
    if request.method == "POST" :
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit = False)
            comment.post = post
            comment.save()
            return redirect('/herby/' + str(post.id))

        else : 
            form = CommentForm()
        return render(request, 'add_comment.html', {'form':form})        


def unifilter(request, myuni):
    # post_detail = get_object_or_404(Blog, pk=post_id)
    unipost = Post.objects.filter(myuni=myuni)
 
    return render(request, 'main.html', {"posts":unipost})