# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.utils import timezone
from django.shortcuts import (
    render,
    redirect,
    get_object_or_404,
)
from .models import Article
from .forms import ArticleForm


def article_new(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.published_at = timezone.now()
            article.save()
            return redirect('blog.views.article_show', pk=article.pk)
    else:
        form = ArticleForm()

    return render(request, 'article_edit.html', {
        'form': form,
    })


def article_show(request, pk):
    article = get_object_or_404(Article, pk=pk)
    return render(request, 'article_show.html', {
        'article': article,
    })


def article_edit(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.publised_at = timezone.now()
            article.save()
            return redirect('blog.views.article_show', pk=article.pk)
    else:
        form = ArticleForm(instance=article)
    return render(request, 'article_edit.html', {
        'form': form,
    })

# def article_show(request, pk):
#     article = get_object_or_404(Article, pk=pk)
#     return render(request, 'article_show.html', {
#         'article': article,
#     })


def article_list(request):
    articles = Article \
        .objects \
        .filter(published_at__lte=timezone.now()) \
        .order_by('published_at')

    return render(request, 'article_list.html', {
        'articles': articles,
    })
