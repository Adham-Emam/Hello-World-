from django.apps import AppConfig


class ForumConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Forum'

    def ready(self):
        from .forum_channels import create_channels

        # Create channels or check for new one
        create_channels()
