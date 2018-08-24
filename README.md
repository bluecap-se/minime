# MiniMe

[![Travis](https://img.shields.io/travis/bluecap-se/minime.svg)](https://travis-ci.org/bluecap-se/minime)
![Status](https://img.shields.io/badge/status-stable-green.svg)
![PyPI - Python Version](https://img.shields.io/badge/python-3.7-blue.svg)
[![Docker pulls](https://img.shields.io/docker/pulls/bluecap/minime.svg)](https://registry.hub.docker.com/u/bluecap/minime/)
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

This project relies on [Pipenv](https://docs.pipenv.org/), ensure that it is
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

## Run tests

### Regular tests

```
$ python manage.py test
```

### Test coverage

```
$ coverage run --source minime -m py.test
$ coverage html
$ open htmlcov/index.html
```

## License

Published under [MIT License](https://github.com/bluecap-se/minime/master/LICENSE).
