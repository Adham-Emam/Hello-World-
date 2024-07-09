from django.urls import path
from . import views

urlpatterns = [
    path('channels/', views.forum, name='forum'),
    path('channel/<int:id>/', views.channel_page, name='channel_page'),
    path('post_page/<int:id>', views.post_page, name='post_page'),
    path('channel_page/<int:id>/add_post/', views.add_post, name='add_post'),
    path('like/<int:id>/', views.like_post, name='like_post')
]
