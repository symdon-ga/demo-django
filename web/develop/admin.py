from django.contrib import admin


from example.core.models import (
    User,
)

from example.counter.models import Counter

admin.site.register(User)
admin.site.register(Counter)
