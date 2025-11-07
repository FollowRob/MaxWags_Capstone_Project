from django.contrib import admin
from .models import User, DogPost, Comment

# Register your models here.
admin.site.register(User)
admin.site.register(DogPost)
admin.site.register(Comment)
