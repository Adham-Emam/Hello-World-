from django.db import models

class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=3000, null=True)
    url = models.URLField(default=None)
    tags = models.CharField(max_length=255, null=True)
    reactions = models.IntegerField(default=0)
    cover_img = models.URLField(null=True)
    reading_time_minutes = models.IntegerField(null=True)
    author = models.CharField(max_length=150, null=True)
    twitter_url = models.URLField(null=True)
    github_url = models.URLField(null=True)
    website_url = models.URLField(null=True)
    profile_image = models.URLField(null=True)
    published_date = models.DateTimeField(null=True)

    def __str__(self):
        return self.title

