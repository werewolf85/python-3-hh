"""
URL configuration for handhunter project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls.py import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls.py'))
"""
from django.contrib import admin
from django.urls import path, include
from core.views import *
from worker.views import *
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage, name='home'),
    path('about/', about),
    path('search/', search, name='search'),
    path('contacts/', contact_view),
    path('address/', address),
    path('vacancies/', vacancy_list),
    path('vacancy/<int:id>/', vacancy_detail, name='vacancy-info'),
    path('add-vacancy-df/', vacancy_add_via_django_form),
    path('vacancy-edit/<int:id>/', vacancy_edit, name='vacancy-edit'),
    path('vacancy-edit-df/', vacancy_edit_df, name='vacancy-edit-df'),
    path('add-vacancy/', vacancy_add),
    path("workers/", workers),
    path("worker/<int:id>/", worker_info),
    path("resume-list/", resume_list),
    path("resume-info/<int:id>/", resume_info),
    path("resume-edit/<int:id>/", resume_edit, name="resume-edit"),
    path("my-resume/", my_resume, name='my-resume'),
    path('resume-edit/<int:id>/', resume_edit, name='resume-edit'),
    path('add-resume/', add_resume, name='add-resume'),
    path('add-resume-df/', resume_add_django_form, name='add-resume-df'),
    path('registration/', reg_view, name='reg'),
    path('sign-in/', sign_in, name='sign-in'),
    path('login-generic/', LoginView.as_view(), name='login-generic'),
    path('sign-out/', sign_out, name='sign-out'),
    path('companies/', company_list),
    path("company-edit-df/<int:id>/", company_edit, name="company-edit"),
    path("company/<int:id>/", company_info, name='company-info'),
    path('add-company-df/', company_add_form, name='add-company-df'),
    path('recruit/', include('recruit.urls')),
    path('news/', include('news.urls'), name='news'),


] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
