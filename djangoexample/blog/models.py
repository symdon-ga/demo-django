# -*- coding: utf-8 -*-
import uuid
import datetime
from django.db import models


class Article(models.Model):
    code = models.UUIDField(primary_key=True, db_index=True, default=uuid.uuid4)
    subject = models.CharField(max_length=0xFF)
    body = models.TextField()
    published_at = models.DateTimeField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_at = datetime.datetime.now()

    def __str__(self):
        return self.subject
