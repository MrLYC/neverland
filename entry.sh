#!/bin/sh

/neverland/manage.py syncdb
/neverland/manage.py create_admin
exec uwsgi --ini /etc/uwsgi.ini
