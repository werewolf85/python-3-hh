from django.urls import path
from .views import *

urlpatterns = [
    path('news-list/', ArticleList.as_view(), name='news-list'),
    path('news-create/', ArticleCreate.as_view(), name='news-create'),
    path('news-detail/<int:pk>/', ArticleDetail.as_view(), name='news-detail'),
    path('news-update/<int:pk>/', ArticleUpdate.as_view(), name='news-update'),
    ]