from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import User, DogPost, Comment

# Create your views here.
def home_page_view(request):
    return render(request, 'home.html')

def register_view(request):
    return render(request, 'register.html')

def login_view(request):
    return render(request, 'login.html')

def logout_view(request):
    return render(request, 'logout.html')

def posts_view(request):
        posts = DogPost.objects.all().order_by('-date_posted') 
        context = {'posts': posts}
        return render(request, 'posts.html', context)
