from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from .models import Post
from .forms import PostForm
from django.contrib.auth.decorators import login_required

# Home view
def home(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'home.html', {'posts': posts})

# Post detail view
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'post_detail.html', {'post': post})

# Create post (login required)
@login_required
def create_post(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            messages.success(request, "Post created successfully!")
            return redirect('home')
    else:
        form = PostForm()
    return render(request, 'create_post.html', {'form': form})

# Guest signup
def guest_signup(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken!")
        else:
            user = User.objects.create_user(username=username, password=password)
            messages.success(request, "Guest account created successfully!")
            login(request, user)
            return redirect('home')
    
    return render(request, 'guest_signup.html')

# Guest login
def guest_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Invalid username or password")
    
    return render(request, 'guest_login.html')

# Logout view
def user_logout(request):
    logout(request)
    return redirect('home')
