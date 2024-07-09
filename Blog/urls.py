from django.contrib import admin
from django.urls import path, include
from BlogPost import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blogpost/', include('BlogPost.urls')),
    path('hello_forum/', include('Forum.urls')),
    path('accounts/', include('Users.urls')),
    path('', views.redirect_to_blogpost, name='redirect_to_blogpost'),
]
