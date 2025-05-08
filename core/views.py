from django.shortcuts import render, get_object_or_404
from education.models import Article
from faq.models import FAQ

def homepage(request):
    articles = Article.objects.all().order_by('-id')[:5]
    faqs = FAQ.objects.filter(published=True)[:5]
    return render(request, 'core/home.html', {
        'articles': articles,
        'faqs': faqs
    })
def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    return render(request, 'core/article_detail.html', {'article': article})

def faq_detail(request, pk):
    faq = get_object_or_404(FAQ, pk=pk)
    return render(request, 'core/faq_detail.html', {'faq': faq})
