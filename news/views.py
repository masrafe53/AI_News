# news/views.py
from django.shortcuts import render
from .models import NewsArticle

def news_list(request):
    news_articles = NewsArticle.objects.all()
    return render(request, 'news/news_list.html', {'news_articles': news_articles})
