from django.apps import AppConfig


class BlogpostConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'BlogPost'

    def ready(self):
        from .article_fetcher import fetch_and_save_articles

        # Fetch and save articles if not already saved
        fetch_and_save_articles()
