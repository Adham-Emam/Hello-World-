# Hello World Blog

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Models](#models)
- [Views](#views)
- [Templates](#templates)
- [JavaScript](#javascript)
- [Styling](#styling)
- [API Integration](#api-integration)
- [Deployment](#deployment)

## Introduction

**Hello World Blog** is a modern blogging platform focused on tech and programming. It offers a user-friendly interface for creating, reading, updating, and deleting blog posts. Users can register, log in, like posts, comment on them, and participate in forum discussions. The project is built using Django and includes several features to enhance user experience.

## Features

- User Authentication (Register, Login, Logout)
- Blog Post Creation and Management
- Liking Posts
- Commenting on Posts
- Forum for Discussions
- Search Functionality
- Responsive Design

## Installation

### Prerequisites

- Python 3.7+
- Django 3.2+

### Steps

1. Clone the repository:

   ```sh
   git clone https://github.com/Adham-Emam/Hello-World-Blog
   cd hello-world-blog
   ```

2. Create and activate a virtual environment:

   ```sh
   python -m venv .venv # On Windows
   source venv/bin/activate # On MacOs
   ```

3. Install the dependencies:

   ```sh
   pip install -r requirements.txt
   ```

4. Set up the database:

   ```sh
   python manage.py migrate
   ```

5. Create a superuser:

   ```sh
   python manage.py createsuperuser
   ```

6. Run the development server:

   ```sh
   python manage.py runserver
   ```

7. Open your browser and navigate to `http://127.0.0.1:8000`.

## Usage

### Models

- **CustomUser**: Extends the default Django user model with additional fields like `bio`.
- **BlogPost**: Represents a blog post with fields for title, content, created_at, created_by, likes, and comments.
- **Channel**: Represents discussion channels in the forum with fields for name and description.
- **Post**: Represents threads within channels with fields for title, created_by, created_at, comments and likes.
- **Comment**: Represents comments on Forum posts with fields for content, created_at, created_by, and the post it belongs to.

### Views

- **Home**: Displays the latest blog posts.
- **Blogs**: Displays all blog posts and allows searching by tags or queries.
- **Blog Page**: Displays a single blog post with its author's data.
- **Register**: Handles user registration.
- **Login**: Handles user login.
- **Logout**: Logs out the user.
- **Hello, Forum!**: Displays all channels.
- **Post Page**: Displays a single thread with its comments.

### Templates

Templates are located in the `templates` directory. Key templates include:

- `layout.html`: Base template with common layout and styles.
- `home.html`: Template for the home page.
- `blogs.html`: Template for displaying all blog posts.
- `blog_page.html`: Template for displaying a single blog post.
- `register.html`: Template for user registration.
- `login.html`: Template for user login.
- `forum.html`: Template for the forum.
- `channel_page.html`: Template for displaying a single thread.
- `post_page.html`: Template for displaying a single post.
- `404.html`:Template fo handling 404 Not found Error
- `500.html`:Template fo handling 500 Internal server error


### Styling

CSS styles are located in the `static/css` directory. Key styles include:

- `styles.css`: Main stylesheet for the application.


### API Integration

Integrate with external APIs to fetch and display relevant data, such as blog posts from other sources.

### Deployment

This app is deployed on heroku, to view the app please visit:
[Hello, World!](https://hello-world-blog0-5f62484886a9.herokuapp.com/blogpost/)
