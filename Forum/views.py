from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.utils import timezone
from .models import Channel, Post, Comment
from .forum_channels import create_channels
from datetime import timedelta


def format_time_difference(time_difference):
    days = time_difference.days
    seconds = time_difference.seconds

    years, days = divmod(days, 365)
    months, days = divmod(days, 30)
    weeks, days = divmod(days, 7)
    hours, seconds = divmod(seconds, 3600)
    minutes, seconds = divmod(seconds, 60)

    if years > 0:
        return f"{years}y"
    elif months > 0:
        return f"{months}m"
    elif weeks > 0:
        return f"{weeks}w"
    elif days > 0:
        return f"{days}d"
    elif hours > 0:
        return f"{hours}h"
    elif minutes > 0:
        return f"{minutes}min"
    else:
        return f"{seconds}s"


def forum(request):
    # Create channels or check for new one
    create_channels()

    channels = Channel.objects.all()

    results = []
    if request.method == 'POST':
        query = request.POST.get('search-channel', '')

        for channel in channels:
            if query.lower() in channel.name.lower():
                results.append(channel)

        context = {
            'channels': results
        }
    else:
        context = {
            'channels': channels
        }
    return render(request, 'Forum/forum.html', context)


def channel_page(request, id):
    channels = Channel.objects.all()

    current_channel = Channel.objects.get(id=id)

    posts = Post.objects.filter(channel=current_channel)[::-1]

    for post in posts:
        time_difference = timezone.now() - post.created_at
        post.created_at = format_time_difference(time_difference)

        if request.user in post.likes.all():
            post.liked = True
        else:
            post.liked = False

    results = []
    if request.method == 'POST':
        query = request.POST.get('search-channel', '')

        for channel in channels:
            if query.lower() in channel.name.lower():
                results.append(channel)
        context = {
            'current_channel': current_channel,
            'channels': results,
            'posts': posts,
        }
    else:
        context = {
            'current_channel': current_channel,
            'channels': channels,
            'posts': posts,
        }

    return render(request, 'Forum/channel_page.html', context)


@login_required
def add_post(request, id):
    current_channel = get_object_or_404(Channel, id=id)

    if request.method == 'POST':
        content = request.POST['post-content']

        if content:
            new_post = Post(content=content, channel=current_channel,
                            created_by=request.user)
            new_post.save()
            messages.success(request, 'Your post has been created 🎉')
        else:
            messages.error(request, "You can't publish an empty post")

    return redirect('channel_page', id=id)


@login_required
def like_post(request, id):
    post = get_object_or_404(Post, id=id)

    if request.user in post.likes.all():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)

    next_url = request.GET.get('next', 'channel_page')

    return redirect(next_url, id=post.channel.id)


@login_required
def add_comment(request, id):
    post = get_object_or_404(Post, id=id)

    if request.method == 'POST':
        comment = request.POST['comment']

        new_comment = Comment(
            content=comment, created_by=request.user, post=post)
        Comment.save(new_comment)

    return redirect('post_page', id=id)


def post_page(request, id):
    post = get_object_or_404(Post, id=id)

    post_time_difference = timezone.now() - post.created_at
    post.created_at = format_time_difference(post_time_difference)

    comments = Comment.objects.filter(post=id)

    for comment in comments:
        comment_time_difference = timezone.now() - comment.created_at
        comment.created_at = format_time_difference(comment_time_difference)

    if request.user in post.likes.all():
        post.liked = True
    else:
        post.liked = False

    context = {
        'post': post,
        'comments': comments
    }
    return render(request, 'Forum/post_page.html', context)
