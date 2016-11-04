#!/bin/bash

/nerverland/manage.py syncdb
/nerverland/manage.py create_admin
exec uwsgi --ini /etc/neverland/uwsgi.ini
