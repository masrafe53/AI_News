# news/management/commands/scrape_news.py
from django.core.management.base import BaseCommand
from news.scraper import scrape_news
from news.models import NewsArticle

class Command(BaseCommand):
    help = 'Scrape news from other websites and save to the database'

    def handle(self, *args, **options):
        news_data = scrape_news()
        for data in news_data:
            NewsArticle.objects.create(
                title=data['title'],
                content=data['content'],
                publication_date=data['publication_date'],
                image_url=data['image_url']
            )
# news/management/commands/scrape_news.py
from django.core.management.base import BaseCommand
from news.tasks import fetch_and_save_news

class Command(BaseCommand):
    help = 'Scrape news from other websites and save to the database'

    def handle(self, *args, **options):
        fetch_and_save_news.delay()
        self.stdout.write(self.style.SUCCESS('Successfully started scraping news in the background.'))
