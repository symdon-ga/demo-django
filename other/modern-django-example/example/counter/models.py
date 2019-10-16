from django.db.models import Model, IntegerField


class Counter(Model):
    count = IntegerField(default=0)

    def increment(self):
        self.count += 1
        return self

    def decrement(self):
        self.count -= 1
        return self
