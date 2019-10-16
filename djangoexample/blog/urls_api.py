from django.conf.urls import url

from . import api

urlpattern = [
    url(r'articles/$', api.ArticleViewSet.as_view({
        'get': 'list',
        'post': 'create',
        'put': 'bulk_create',
        }), name='api.article'),

    url(r'articles/(?P<pk>[^/]+)', api.ArticleViewSet.as_view({
        'get': 'retrieve',
        'post': 'update',
        'delete': 'destroy',
        }), name='api.article.detail'),
]
