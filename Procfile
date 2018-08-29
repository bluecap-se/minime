release: python manage.py migrate --noinput && python manage.py compilestatic --delete-stale-files
web: gunicorn app.wsgi
