# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import (
    Article,
    )

_register_classes = (
    Article,
)

for cls in _register_classes:
    admin.site.register(cls)
