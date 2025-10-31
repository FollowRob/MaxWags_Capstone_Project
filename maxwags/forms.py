from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, DogPost

# Registration form
class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

# Post upload form (DogPost)
class DogPostForm(forms.ModelForm):
    class Meta:
        model = DogPost
        fields = ['image', 'caption']
        widgets = {
            'caption': forms.TextInput(attrs={'placeholder': 'Add a caption...'}),
        }