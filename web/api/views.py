from django.db import transaction
from rest_framework.decorators import detail_route
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from example.core.models import User
from example.counter.models import Counter


from .actions import CounterAction
from .serializers import (
    UserSerializer,
    CounterSerializer,
)


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CounterViewSet(ModelViewSet):
    queryset = Counter.objects.all()
    serializer_class = CounterSerializer

    @detail_route(methods=['GET'])
    @transaction.atomic
    def increment(self, *args, **kwargs):
        serializer = self._perform_action(CounterAction.increment, *args, **kwargs)
        return Response(serializer.data)

    @detail_route(methods=['GET'])
    @transaction.atomic
    def decrement(self, *args, **kwargs):
        serializer = self._perform_action(CounterAction.decrement, *args, **kwargs)
        return Response(serializer.data)


    def _perform_action(self, action, request, pk=None, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        serializer.perform_action(action)

        if getattr(instance, '_prefetched_objects_cache', None):
            instance._prefetched_objects_cache = {}

        return serializer
