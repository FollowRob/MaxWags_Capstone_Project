from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_page_view(request):
    return HttpResponse('<h1>Welcome to the MaxWags Home Page!</h1>')

def register_view(request):
    return HttpResponse('<h1>Register for an account</h1>')

def login_view(request):
    return HttpResponse('<h1>Login</h1>')

def logout_view(request):
    return HttpResponse('<h1>Logout</h1>')

def posts_view(request):
    return HttpResponse('<h1>Posts</h1>')
