from django.contrib import admin
from .models import Vacancy, Company, Category
# Register your models here.
# admin.site.register(Vacancy)
admin.site.register(Company)
admin.site.register(Category)

@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'salary', 'is_relevant', 'contacts']
    search_fields = ['title', 'description', 'candidate__name', 'candidate__user__username']
    list_filter = ['category', 'salary', 'is_relevant']
    list_editable = ['title', 'is_relevant', 'contacts']