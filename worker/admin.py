from django.contrib import admin
from .models import Worker
from .models import Comment

# Register your models here.
admin.site.register(Worker)
admin.site.register(Comment)
