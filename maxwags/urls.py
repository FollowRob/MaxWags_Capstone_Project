from django.urls import path
from .views import (
    home_page_view,
    register_view,
    login_view,
    logout_view,
    posts_view,
    add_comment_view,
    create_dog_post_view
)

urlpatterns = [
    path('', home_page_view, name='home'),
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('posts/', posts_view, name='posts'),
    path('posts/<int:post_id>/comment/', add_comment_view, name='add_comment'),
    path('upload/', create_dog_post_view, name='create_post'),
]
