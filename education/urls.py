from django.urls import path
from . import views

urlpatterns = [
    path('article/<int:pk>/', views.article_detail, name='article_detail'),
]
