from django.contrib import admin
from .models import BlogPost


class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_date',
                    'reactions', 'reading_time_minutes')
    search_fields = ('title', 'author', 'tags')
    list_filter = ('published_date', 'reactions')
    ordering = ('-published_date',)
    fields = ('title', 'description', 'url', 'tags', 'reactions', 'cover_img',
              'reading_time_minutes', 'author', 'twitter_url', 'github_url',
              'website_url', 'profile_image', 'published_date')
    readonly_fields = ('reactions', 'published_date')

    def save_model(self, request, obj, form, change):
        if not obj.published_date:
            obj.published_date = timezone.now()
        obj.save()


admin.site.register(BlogPost, BlogPostAdmin)
