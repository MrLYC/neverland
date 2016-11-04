#!/usr/bin/env python
# coding=utf-8

from django.contrib.auth import models

class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        if not models.User.objects.all().exists():
            admin = User(username="admin")
            admin.set_password("admin")
            admin.is_superuser = True
            admin.is_staff = True
            admin.save()

