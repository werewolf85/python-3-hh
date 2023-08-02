from django.shortcuts import render, HttpResponse
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, DetailView
from django.urls import reverse_lazy
from .models import ArticleNew
from .forms import ArticleNewForm

# Create your views here.
class ArticleList(ListView):
    model = ArticleNew
    template_name = 'news/list_news.html'
    context_object_name = 'articles'

class ArticleDetail(DetailView):
    model = ArticleNew
    template_name = 'news/detail_news.html'
    context_object_name = 'article'

    def get(self, request):
        article = self.get_object()
        article.views_count += 1
        article.save()
        return super().get(request)

class ArticleCreate(CreateView):
    model = ArticleNew
    template_name = 'news/edit_news.html'
    fields = ['author', 'title', 'text']
    success_url = reverse_lazy('news-list')

class ArticleUpdate(UpdateView):
    model = ArticleNew
    template_name = 'news/edit_news.html'
    fields = ['title', 'text']
    success_url = reverse_lazy('news-list')