# -*- coding: utf-8 -*-
from datetime import datetime
from django.db import models

# Create your models here.
class Article(models.Model):
    subject = models.CharField(max_length=0xFF)
    body = models.TextField()

    published_at = models.DateTimeField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_at = datetime.now()

    def __str__(self):
        return self.subject
