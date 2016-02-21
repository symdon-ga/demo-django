from django.conf.urls import url, include

from . import urls_api

urlpatterns = [
    # url(r'articles/?$', views.article_list),
    # url(r'articles/new/?$', views.article_new),
    # url(r'articles/edit/(?P<pk>[0-9]+)/?$', views.article_edit),
    # url(r'articles/show/(?P<pk>[0-9]+)/?$', views.article_show),
    url(r'api', include(urls_api.urlpattern)),
]
