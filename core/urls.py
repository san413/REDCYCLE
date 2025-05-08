from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('article/<int:pk>/', views.article_detail, name='article_detail'),
    path('faq/<int:pk>/', views.faq_detail, name='faq_detail'),
]
