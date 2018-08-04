# MiniMe

[![Travis](https://img.shields.io/travis/bluecap-se/minime.svg)](https://travis-ci.org/bluecap-se/minime)
![Status](https://img.shields.io/badge/status-WIP-orange.svg)
![PyPI - Python Version](https://img.shields.io/badge/python-3.7-blue.svg)
![Platform](https://img.shields.io/badge/platform-win%20%7C%20lin%20%7C%20osx-lightgrey.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

The last link shortener you'll need.

## Install and run

### Run with Docker

The preferred method is to run the project inside a Docker container.
There are currently no images available on Docker Hub, but it's easy to build.

```
$ git clone git@github.com:bluecap-se/minime.git
$ cd minime
$ docker build -t bluecap/minime .
$ docker run -d -p 80:8000 bluecap/minime:latest
$ open localhost
```

## Run on local machine

This project relies on [Pipenv](https://docs.pipenv.org/), ensure that it is
installed with `pip install pipenv` first.

```
$ git clone git@github.com:bluecap-se/minime.git
$ cd minime
$ pipenv install --three
$ pipenv shell
$ python manage.py runserver &
$ open http://127.0.0.1:8000/
```

## Run tests

### Regular tests

```
$ pipenv install --dev
$ py.test
```

### Watch for changes

To run the tests continuously, run the test command with the watch or follow flag `-f`:

```
$ py.test -f
```

### Test coverage

```
$ coverage run --source minime -m py.test
$ coverage html
$ open htmlcov/index.html
```

## License

Published under [MIT License](https://github.com/bluecap-se/minime/master/LICENSE).
