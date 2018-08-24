#!/bin/bash

set -eu

if [ "$1" = 'runwsgi' ]; then
	exec uwsgi --ini /minime/uwsgi.ini --uid=1000 --gid=2000
elif [ "$1" = 'runserver' ]; then
	exec python /minime/manage.py runserver 0.0.0.0:8000
elif [ "$1" = 'test' ]; then
	exec python /minime/manage.py test
fi

exec $@
