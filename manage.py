#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "neverland.settings")
    os.environ.setdefault("DEBUG", "1")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
