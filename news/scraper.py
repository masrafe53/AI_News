# news/scraper.py
import requests
from bs4 import BeautifulSoup
from datetime import datetime
from .models import NewsArticle

def scrape_news():
    url = 'https://www.bbc.com/news'
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        articles = soup.find_all('article')
        news_data = []
        for article in articles:
            title = article.find('h2').get_text()
            content = article.find('div', class_='content').get_text()
            publication_date_str = article.find('time').get_text()
            publication_date = datetime.strptime(publication_date_str, '%Y-%m-%d').date()
            image_url = article.find('img')['src']
            news_data.append({
                'title': title,
                'content': content,
                'publication_date': publication_date,
                'image_url': image_url
            })
        return news_data
    else:
        print(f"Failed to fetch news. Status code: {response.status_code}")
        return []
