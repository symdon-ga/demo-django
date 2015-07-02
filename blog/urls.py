# -*- coding: utf-8 -*-
from django.conf.urls import include, url
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^ping/', views.ping),
    url(r'^articles/?$', views.article_list),
    url(r'^articles/new/?$', views.article_new),
    url(r'^articles/edit/(?P<pk>[0-9]+)/?$', views.article_edit),
    url(r'^articles/show/(?P<pk>[0-9]+)/?$', views.article_show),
]
