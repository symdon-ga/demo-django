# -*- coding: utf-8 -*-
from django import forms
from .models import Article


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('subject', 'body')
