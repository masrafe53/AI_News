# news/models.py
from django.db import models

class NewsArticle(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    publication_date = models.DateTimeField()
    image_url = models.URLField()

    def __str__(self):
        return self.title
