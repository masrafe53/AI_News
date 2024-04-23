# news/tasks.py
from celery import shared_task
from .scraper import scrape_news
from .models import NewsArticle

@shared_task
def fetch_and_save_news():
    news_data = scrape_news()
    for data in news_data:
        NewsArticle.objects.create(
            title=data['title'],
            content=data['content'],
            publication_date=data['publication_date'],
            image_url=data['image_url']
        )
