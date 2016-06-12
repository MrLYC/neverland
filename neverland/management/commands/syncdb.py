#!/usr/bin/env python
# coding=utf-8

from django.apps import apps
from django.core.management import call_command
from django.core.management.base import BaseCommand


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        app_name_lst = [i.label for i in apps.get_app_configs()]
        call_command("makemigrations", *app_name_lst)
        call_command("migrate")
