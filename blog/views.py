# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.utils import timezone
from django.shortcuts import (
    render,
    get_object_or_404,
)
from .models import Article
from .forms import ArticleForm

# Create your views here.
def ping(request):
    return HttpResponse('PONG')


def article_new(request):
    form = ArticleForm()
    return render(request, 'article_edit.html', {
        'form': form,
    })


def article_show(request, pk):
    article = get_object_or_404(Article, pk=pk)
    return render(request, 'article_show.html', {
        'article': article,
    })


def article_list(request):
    articles = Article \
        .objects \
        .filter(published_at__lte=timezone.now()) \
        .order_by('published_at')

    return render(request, 'article_list.html', {
        'articles': articles,
    })
