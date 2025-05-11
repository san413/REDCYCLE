from django.shortcuts import render, get_object_or_404, redirect
from .models import Article
from .forms import CommentForm

def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    comments = article.comments.order_by('-created_at')
    form = CommentForm()

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.article = article
            new_comment.save()
            return redirect('article_detail', pk=article.pk)

    return render(request, 'education/article_detail.html', {
        'article': article,
        'comments': comments,
        'form': form
    })
