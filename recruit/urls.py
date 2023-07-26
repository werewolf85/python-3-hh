from django.urls import path
from .views import *



urlpatterns = [
    path('list/', recruiter_list, name='recruiter-list'),
    path('create-recruit/', create_recruit, name='create-recruit'),
    path('recruit-edit/<int:id>/', recruit_update, name='recruit-edit'),
    path('list-class/', RecruitView.as_view(), name='recruiter-list-class'),
    path('list-class-generic/', RecruitListView.as_view(), name='recruiter-list-class-generic'),
    path('detail/<int:pk>/', recruiter_detail, name='recruiter-detail'),
    path('create/', RecruiterCreateView.as_view(), name='create-recruiter'),
]
