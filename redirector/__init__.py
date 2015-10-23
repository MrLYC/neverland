import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "redirector.settings")
django.setup()
