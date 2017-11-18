from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin

from rest_framework_jwt.views import obtain_jwt_token

from .api import urls as api_urls

urlpatterns = [
    url(r'^api/', include(api_urls)),
    url(r'^auth/token/', obtain_jwt_token),
]

if settings.DEBUG:
    urlpatterns += [
        url(r'^admin/', admin.site.urls)
    ]
