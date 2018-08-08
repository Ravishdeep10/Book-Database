from django.db import models


class Article(models.Model):
    id = models.IntegerField(primary_key=True)
    author = models.CharField(max_length=32)
    title = models.CharField(max_length=32)
    content = models.CharField(max_length=2048)
    image = models.CharField(max_length=200)
    isbn = models.CharField(max_length=200)
