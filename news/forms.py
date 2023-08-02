from django import forms
from .models import ArticleNew

class ArticleNewForm(forms.ModelForm):
    class Meta:
        model = ArticleNew
        fields = '__all__'