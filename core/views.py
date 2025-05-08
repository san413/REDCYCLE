from django.shortcuts import render, get_object_or_404
from education.models import Article, Video  # No FAQ import here from education
from faq.models import FAQ  # Import FAQ from faq.models

def homepage(request):
    articles = Article.objects.all().order_by('-id')[:5]
    faqs = FAQ.objects.filter(published=True)[:5]
    videos = Video.objects.filter(published=True)[:3]  # Fetch the latest 3 published videos
    return render(request, 'core/home.html', {
        'articles': articles,
        'faqs': faqs,
        'videos': videos  # Pass videos to the template
    })

def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    return render(request, 'core/article_detail.html', {'article': article})

def faq_detail(request, pk):
    faq = get_object_or_404(FAQ, pk=pk)
    return render(request, 'core/faq_detail.html', {'faq': faq})

def articles_by_category(request, category_slug):
    articles = Article.objects.filter(category=category_slug, published=True)
    return render(request, 'core/articles_by_category.html', {
        'articles': articles,
        'category': category_slug
    })
