#!/bin/bash

set -eu

if [ "$1" = 'runproduction' ]; then
	python /minime/manage.py collectstatic --noinput
	exec gunicorn app.wsgi -b 0.0.0.0:8000
elif [ "$1" = 'runserver' ]; then
	exec python /minime/manage.py runserver 0.0.0.0:8000
elif [ "$1" = 'test' ]; then
	exec python /minime/manage.py test
fi

exec $@
