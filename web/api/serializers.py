from rest_framework.serializers import ModelSerializer

from example.core.models import User
from example.counter.models import Counter

from .actions import CounterAction
from .exc import CounterOperationError


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'is_active', 'date_joined')


class CounterSerializer(ModelSerializer):
    class Meta:
        model = Counter
        fields = '__all__'

    def perform_action(self, action):
        if not self.instance:
            raise CounterOperationError()

        if action == CounterAction.increment:
            self.instance.increment().save()
        elif action == CounterAction.decrement:
            self.instance.decrement().save()
        return self.instance
