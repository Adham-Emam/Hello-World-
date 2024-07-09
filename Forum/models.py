from django.contrib.auth import get_user_model
from django.db import models
from Users.models import CustomUser
from django.utils import timezone


User = get_user_model()


class Channel(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    channel = models.ForeignKey(
        Channel, related_name='posts', on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    created_by = models.ForeignKey(
        CustomUser, related_name='posts', on_delete=models.CASCADE)
    likes = models.ManyToManyField(
        User, related_name='liked_posts', blank=True)

    def __str__(self):
        return self.created_by.username

    def total_likes(self):
        return self.likes.count()

    def total_comments(self):
        return self.comments.count()


class Comment(models.Model):
    post = models.ForeignKey(
        Post, related_name='comments', on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    created_by = models.ForeignKey(
        CustomUser, related_name='comments', on_delete=models.CASCADE)

    def __str__(self):
        return self.created_by.username
