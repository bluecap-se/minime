#!/bin/bash

set -e

if [ "$1" = 'runserver' ]; then
	exec minime "$@"
fi

exec "$@"
