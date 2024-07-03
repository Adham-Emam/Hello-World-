from django.conf.urls import handler400, handler403, handler404, handler500
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('/blogs', views.blogs, name='blogs'),
    path('/blogs/<str:tag>', views.search_tag, name='search'),
    path('/blogs/', views.search_query, name='search_query'),
    path('/blog/<int:id>', views.blog_page, name='blog_page'),
    path('register', views.regiester, name='register'),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
]
