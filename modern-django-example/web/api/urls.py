from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
# from rest_framework_nested.routers import NestedDefaultRouter

from .views import (
    UserViewSet,
    CounterViewSet,
)

router = DefaultRouter()
router.register(r'user', UserViewSet)
router.register(r'counter', CounterViewSet)


# counter_router = NestedDefaultRouter(router, r'counter', lookup='counter')
# counter_router.register(r'counter', CoutnerViewSet)


urlpatterns = [
] + router.urls
