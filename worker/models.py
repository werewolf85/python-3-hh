from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Worker(models.Model):
    user = models.OneToOneField(
        to=User,
        null=True,
        blank=False,
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=50)
    specialization = models.CharField(max_length=255)
    need_salary = models.IntegerField(null=True, blank=True)
    is_searching = models.BooleanField(default=True)
    def __str__(self):
        return self.name

class Comment(models.Model):
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    worker = models.ForeignKey(
        to=Worker,
        on_delete=models.CASCADE
    )
    author = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.author.username


