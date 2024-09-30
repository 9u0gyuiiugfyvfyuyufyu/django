# blog/models.py
from django.db import models
from django.utils import timezone

class Post(models.Model):  # Change 'post' to 'Post' (PascalCase)
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title