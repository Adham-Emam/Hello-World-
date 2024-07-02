from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .form import CustomUserCreationForm
from .models import BlogPost
from .article_fetcher import ArticleFetcher


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


def home(request):
    # Fetch and save articles if not already saved
    fetch_and_save_articles()

    # Query BlogPost objects to display in the template
    articles = BlogPost.objects.all()

    latest_articles = []

    for article in articles:
        if article.cover_img:
            latest_articles.append(article)
            if len(latest_articles) == 5:
                break

    for article in articles:
        if len(article.title) > 40:
            article.title = f"{article.title[:40].strip()}..."

        article.tags = article.tags.split(', ')[:3]

    context = {
        'articles': latest_articles
    }
    return render(request, 'home.html', context)


def blogs(request):
    articles = BlogPost.objects.all()

    for article in articles:
        if len(article.title) > 40:
            article.title = f"{article.title[:40].strip()}..."

        article.tags = article.tags.split(', ')[:3]

    context = {
        'articles': articles
    }
    return render(request, 'blogs.html', context)


def search_results(request, tag):
    articles = BlogPost.objects.all()

    results = [article for article in articles if tag in article.tags]

    for article in results:
        article.tags = article.tags.split(', ')[:3]

    context = {
        'articles': results,
        'title': f'Search Results for: {tag}'
    }
    return render(request, 'blogs.html', context)


def blog_page(request, id):
    article = BlogPost.objects.get(id=id)

    article.tags = article.tags.split(', ')

    return render(request, 'blog_page.html', {"article": article})


def regiester(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration successful.')
            return redirect('login')
        else:
            messages.error(
                request, 'Registration failed. Please correct the error below.')
    else:
        form = CustomUserCreationForm()

    return render(request, 'regiester.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'login.html')


@login_required
def logout_view(request):
    logout(request)
    return redirect('home')
