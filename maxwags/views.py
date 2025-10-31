from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import User, DogPost, Comment
from .forms import DogPostForm


# Create your views here.
def home_page_view(request):
    return render(request, 'home.html')

# Anyone is able to register
def register_view(request):
    from .forms import RegisterForm
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_walker = False  # Default to False, superadmin/walkers need to assign role
            user.save()
            login(request, user)
            messages.success(request, "Thanks for signing up!")
            return redirect('posts')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

# Log in
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('posts')
        else:
             messages.error(request, 'Invalid username or password.')
    return render(request, 'login.html')

# Log out
def logout_view(request):
    logout(request)
    messages.info(request, 'You have successfully logged out.')
    return redirect('home')

# Posts - viewable by any user
def posts_view(request):
    posts = DogPost.objects.all().order_by('-date_posted')
    return render(request, 'posts.html', {'posts': posts})

# Add comment - logged in users only
@login_required
def add_comment_view(request, post_id):
    post = get_object_or_404(DogPost, id=post_id)

    if request.method == 'POST':
        text = request.POST.get('text')
        if text:
            Comment.objects.create(
                post=post,
                user=request.user,
                text=text,
            )
            messages.success(request, 'Comment added successfully.')
        else:
            messages.error(request, 'Comment cannot be empty.')
    return redirect('posts')

# Check walker status
def is_walker(user):
    return user.is_authenticated and user.is_walker

# Add Dog Post - walkers only
@user_passes_test(is_walker, login_url='home')
def create_dog_post_view(request):
    if request.method == 'POST':
        form = DogPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            messages.success(request, 'Post created successfully.')
            return redirect('posts')
    else:
        form = DogPostForm()
    return render(request, 'create_post.html', {'form': form})