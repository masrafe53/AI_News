# news_website/news_website/celery.py

import os
from celery import Celery

# Set the Django settings module for Celery
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'news_website.settings')

# Create a Celery application
app = Celery('news_website')

# Load configuration from Django settings
app.config_from_object('django.conf:settings', namespace='CELERY')

# Automatically discover tasks in Django apps
app.autodiscover_tasks()
