#!/bin/bash

/neverland/manage.py syncdb
/neverland/manage.py create_admin
exec uwsgi --ini /etc/neverland/uwsgi.ini
