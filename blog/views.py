# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.utils import timezone
from django.shortcuts import render
from .models import Article

# Create your views here.
def ping(request):
    return HttpResponse('PONG')


def article_list(request):
    articles = Article \
        .objects \
        .filter(published_at__lte=timezone.now()) \
        .order_by('published_at')

    return render(request, 'article_list.html', {
        'articles': articles,
    })
