from django import forms
from .models import Vacancy
from .models import Company


class VacancyForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control my-input"}))
    class Meta:
        model = Vacancy
        fields = [
            'title',
            'salary',
            'description',
            'email',
            'contacts'
        ]


class VacancyEditForm(forms.ModelForm):
    class Meta:
        model = Vacancy
        fields = [
            'title',
            'salary',
            'description',
            'email',
            'contacts'
        ]

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = [
            'name_company',
            'address',
            'count_staff'
        ]


class CompanyEditForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = [
            'name_company',
            'address',
            'count_staff'
        ]