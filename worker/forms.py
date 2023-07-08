from django import forms
from .models import Resume


class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = [
            'title',
            'text'
        ]


class ResumeEditForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = ['title',
                  'text'
        ]


