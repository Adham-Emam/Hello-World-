import requests
from .models import BlogPost


class ArticleFetcher:
    def __init__(self):
        pass

    def get_devto_articles(self):
        url = "https://dev.to/api/articles?tag=programming"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        return []

    def aggregate_articles(self):
        articles = self.get_devto_articles()

        return articles


def fetch_and_save_articles():
    fetcher = ArticleFetcher()
    articles = fetcher.aggregate_articles()

    for post in articles:
        defaults = {
            'title': post['title'],
            'description': post['description'],
            'tags': post['tags'],
            'reactions': post['positive_reactions_count'],
            'cover_img': post['cover_image'],
            'reading_time_minutes': post['reading_time_minutes'],
            'author': post['user']['name'],
            'twitter_url': f"https://x.com/{post['user']['twitter_username']}",
            'github_url': f"https://github.com/{post['user']['github_username']}",
            'website_url': post['user']['website_url'],
            'profile_image': post['user']['profile_image'],
            'published_date': post['published_timestamp']
        }

        blog_post, created = BlogPost.objects.get_or_create(
            url=post['url'],
            defaults=defaults
        )

        if not created:
            # Check if any field has changed
            needs_update = False
            for key, value in defaults.items():
                if getattr(blog_post, key) != value:
                    setattr(blog_post, key, value)
                    needs_update = True

            if needs_update:
                blog_post.save()
