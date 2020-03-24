# MiniMe

[![Travis](https://img.shields.io/travis/bluecap-se/minime.svg)](https://travis-ci.org/bluecap-se/minime)
![Status](https://img.shields.io/badge/status-stable-brightgreen.svg)
[![Coverage Status](https://coveralls.io/repos/github/bluecap-se/minime/badge.svg?branch=develop&gh)](https://coveralls.io/github/bluecap-se/minime?branch=develop)
![PyPI - Python Version](https://img.shields.io/badge/python-3.7-blue.svg)
[![Docker pulls](https://img.shields.io/docker/pulls/bluecap/minime)](https://hub.docker.com/r/bluecap/minime)
![Platform](https://img.shields.io/badge/platform-win%20%7C%20lin%20%7C%20osx-lightgrey.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

The last link shortener you'll ever need.

## Install and run

### Run with Docker

The preferred method is to run the project inside a Docker container.

```
$ git clone git@github.com:bluecap-se/minime.git
$ cd minime
$ docker-compose up -d
$ open http://127.0.0.1:8000/
```

## Run on local machine

This project relies on [Pipenv](https://pipenv.pypa.io/en/latest/), ensure that it is
installed with `pip install pipenv` first.

```
$ git clone git@github.com:bluecap-se/minime.git
$ cd minime
$ pipenv install --three
$ pipenv shell
$ python manage.py migrate
$ python manage.py runserver &
$ open http://127.0.0.1:8000/
```

## Deployment

This project is setup to be deployed on AWS using [Zappa](https://github.com/Miserlou/Zappa).

These environment variables are available:

Variable              | Description                   | Default
--------------------- | ----------------------------- | -------------
DJANGO_DEBUG          | Debug mode                    | False
DJANGO_SECRET_KEY     | Secret key                    | Change!
DJT_ENABLED           | Should DJT be shown?          | False
DATABASE_URL          | Database url                  | Local SQLite
REDIS_URL             | URL to local redis cache      | Local redis
SENTRY_DNS            | URL for Sentry error tracking | None
ALLOWED_HOSTS         | Set to your domain            | Django default

## Run tests

### Regular tests

Tests can be run in Docker or on the host.

```
$ python manage.py test
```

...or in a running docker container:

```
$ docker exec mini_app python manage.py test
```

### Test coverage

```
$ pipenv install --dev
$ coverage run --source='.' manage.py test app.minime
$ coverage html
$ open htmlcov/index.html
```

## License

Published under [MIT License](https://github.com/bluecap-se/minime/master/LICENSE).
