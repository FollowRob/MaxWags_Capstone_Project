from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

# User model
class User(AbstractUser):
    is_walker = models.BooleanField(default=False)

    def __str__(self):
        return self.username
    
# DogPost model
class DogPost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='dog_posts')
    image = models.ImageField(upload_to='dog_images/')
    caption = models.CharField(max_length=120, blank=True)
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}'s post on {self.date_posted.strftime('%d-%m-%Y %H:%M:%S')}"
    
# Comment model
class Comment(models.Model):
    post = models.ForeignKey(DogPost, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user.username} on {self.post.id}"