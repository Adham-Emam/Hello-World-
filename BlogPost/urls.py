from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('blogs', views.blogs, name='blogs'),
    path('blogs/<str:tag>', views.search_tag, name='search'),
    path('blogs/', views.search_query, name='search_query'),
    path('blog/<int:id>', views.blog_page, name='blog_page'),
    path('hello_forum', views.forum, name='forum'),
    path('channel_page/<int:id>', views.channel_page, name='channel_page'),
    path('register', views.regiester, name='register'),
    path(r'^login/$', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
]
