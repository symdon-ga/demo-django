# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.
class Article(models.Model):
    subject = models.CharField(max_length=0xFF)
    body = models.TextField()

    published_at = models.DateTimeField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.subject
