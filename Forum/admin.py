from django.contrib import admin
from .models import Channel, Post, Comment

class ChannelAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)
    fields = ('name', 'description')

class PostAdmin(admin.ModelAdmin):
    list_display = ('content', 'created_by', 'created_at', 'channel', 'total_likes', 'total_comments')
    search_fields = ('content', 'created_by__username', 'channel__name')
    list_filter = ('created_at', 'channel')
    ordering = ('-created_at',)
    fields = ('channel', 'content', 'created_by', 'likes')
    readonly_fields = ('created_at',)

    def total_likes(self, obj):
        return obj.likes.count()
    total_likes.short_description = 'Likes'

    def total_comments(self, obj):
        return obj.comments.count()
    total_comments.short_description = 'Comments'

class CommentAdmin(admin.ModelAdmin):
    list_display = ('content', 'created_by', 'created_at', 'post')
    search_fields = ('content', 'created_by__username', 'post__content')
    list_filter = ('created_at', 'post')
    ordering = ('-created_at',)
    fields = ('post', 'content', 'created_by')
    readonly_fields = ('created_at',)

admin.site.register(Channel, ChannelAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
