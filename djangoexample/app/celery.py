from __future__ import absolute_import

import os

from celery import (
    Celery,
    shared_task,
    )
from celery_once import QueueOnce

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')

from django.conf import settings  # noqa

app = Celery('djangoexample')

app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


@shared_task(base=QueueOnce, once={'graceful': True})
def debug_task():
    print('OK')
