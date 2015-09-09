#!/bin/bash
set -e

if [ "$1" = 'runserver' ]; then
	exec gosu minime "$@"
fi

exec "$@"
