from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
# from rest_framework_nested import routers

from .views import (
    UserViewSet,
)

router = DefaultRouter()
router.register(r'user', UserViewSet)


urlpatterns = [
] + router.urls
