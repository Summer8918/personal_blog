from flask import Flask, render_template, request, redirect, url_for
import os
import json
from datetime import datetime
import re

app = Flask(__name__)
DATA_DIR = 'data'

@app.route('/')
# @app.route() is a decorator that tells flash, when someone visits this URL, run the function below.
def index():
    # Fetch list of articles from files or DB
    articles = load_articles()
    # return "index page"
    # The 'articles' is passed to Jinja2 template block, which is how Flask dynamically generates
    # HTML from Python data
    return render_template("index.html", articles=articles)

@app.route('/article/<slug>')
def article(slug):
    # Load article by slug or ID
    article_data = load_article(slug)
    return render_template('article.html', article=article_data)

# Admin dashboard
@app.route('/admin')
def admin_dashboard():
    articles = load_articles()
    return render_template('admin_dashboard.html', articles=articles)

# It tells Flask how to handle different kinds of HTTP requests for the URL /admin/add.
# Get: Used to get data from the server (like loading a page)
# Post: Used to send data to the server (like submitting a form)
@app.route('/admin/add', methods=['GET', 'POST'])
def add_article():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        save_article(title, content)
        return redirect(url_for('admin_dashboard'))
    return render_template('add_article.html')

@app.route('/admin/edit/<slug>', methods=['GET', 'POST'])
def edit_article(slug):
    if request.method == 'POST':
        # Save complete—take the user back to the dashboard
        updated_title = request.form['title']
        updated_content = request.form['content']
        update_article(slug, updated_title, updated_content)
        # url_for is used to find the URL path for the admin_dashboard function
        # redirect is used to send the browser to that URL (a new request)
        return redirect(url_for('admin_dashboard'))
    article = load_article(slug)
    return render_template('edit_article.html', article=article)

# Utility to create a slug from a title
def slugify(title):
    slug = title.lower()
    slug = re.sub(r'[^a-z0-9]+', '-', slug).strip('-')
    return slug

# Save a new article to a JSON file
def save_article(title, content):
    slug = slugify(title)
    article = {
        "title": title,
        "slug": slug,
        "content": content,
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M")
    }
    filepath = os.path.join(DATA_DIR, f"{slug}.json")
    with open(filepath, 'w') as f:
        json.dump(article, f, indent=4)
    return slug

# Load one article by slug
def load_article(slug):
    filepath = os.path.join(DATA_DIR, f"{slug}.json")
    if not os.path.exists(filepath):
        return None
    with open(filepath, 'r') as f:
        article = json.load(f)
    return article

# Load all articles (for home/admin dashboard)
def load_articles():
    articles = []
    for filename in os.listdir(DATA_DIR):
        if filename.endswith('.json'):
            with open(os.path.join(DATA_DIR, filename), 'r') as f:
                article = json.load(f)
                articles.append(article)
    # Optional: sort by created_at, newest first
    articles.sort(key=lambda x: x['created_at'], reverse=True)
    return articles

if __name__ == '__main__':
    app.run(debug=True)
