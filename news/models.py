from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ArticleNew(models.Model):
    author = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='article_new_object')
    title = models.CharField(max_length=255)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    views_count = models.IntegerField(default=0)
    likes_users = models.ManyToManyField(
        to=User,
        blank=True,
    )

    def __str__(self):
        return self.title
