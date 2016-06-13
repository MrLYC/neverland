#!/usr/bin/env python
# coding=utf-8

from optparse import make_option

from django.apps import apps
from django.core.management import call_command
from django.core.management.base import BaseCommand

import bjoern

from neverland import wsgi


class Command(BaseCommand):
    option_list = BaseCommand.option_list + (
        make_option(
            "-p", "--port", default=8080, help="port to listen",
        ),
        make_option(
            "-a", "--address", default="0.0.0.0", help="address to listen",
        ),
    )

    def handle(self, address, port, *args, **kwargs):
        bjoern.run(wsgi.application, address, port)
