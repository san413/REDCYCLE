from django.shortcuts import render
from education.models import Article
from faq.models import FAQ

def homepage(request):
    articles = Article.objects.all().order_by('-id')[:5]
    faqs = FAQ.objects.filter(published=True)[:5]
    return render(request, 'core/home.html', {
        'articles': articles,
        'faqs': faqs
    })
