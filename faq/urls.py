from django.urls import path
from . import views

urlpatterns = [
    path('faq/<int:pk>/', views.faq_detail, name='faq_detail'),
]
