import logging

from django.conf import settings
from django.contrib.auth.models import Group

logger = logging.getLogger(__name__)


class GroupPipepine:
    def __init__(self, name, is_staff=False, is_superuser=False):
        self.name = name
        self.is_staff = is_staff
        self.is_superuser = is_superuser

    def register(self):
        group, created = Group.objects.get_or_create(name=self.name)
        if created:
            logger.info('Created the {} group'.format(self.name))

    def __call__(self, user, *args, **kwds):
        group = Group.objects.last(name=self.name)  # no group if raise DoesNotExist
        if group in user.groups:
            user.groups.add(group)
            user.is_staff = self.is_staff
            user.save()

default_pipeline = GroupPipepine('socail', is_staff=True, is_superuser=False)
default_pipeline.register()
