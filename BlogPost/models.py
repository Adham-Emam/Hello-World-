from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    # profile_img = models.ImageField(
    #     upload_to='profile_img/', blank=True, null=True)
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.username


class BlogPost(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField()
    image = models.ImageField(upload_to='blog_images/', blank=True, null=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    content = models.TextField(max_length=5000)
    blog_post = models.ForeignKey(
        BlogPost, related_name='comments', on_delete=models.CASCADE)

    def __str__(self):
        return f'Comment by {self.user.username} on {self.blog_post.title}'
