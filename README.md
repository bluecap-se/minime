# MiniMe

[![Circle CI](https://img.shields.io/circleci/project/bluecap-se/minime.svg?style=flat-square)](https://circleci.com/gh/bluecap-se/minime)
[![Dependency Status](https://img.shields.io/gemnasium/bluecap-se/minime.svg?style=flat-square)](https://gemnasium.com/bluecap-se/minime)
[![Docker pulls](https://img.shields.io/docker/pulls/bluecap/minime.svg?style=flat-square)](https://registry.hub.docker.com/u/bluecap/minime/)

An online URL shortener.

## Install

### Using Docker

```console
$ docker run -d -p 80:8000 bluecap/minime:latest
```

### From source

```console
$ git clone https://github.com/bluecap-se/minime.git
$ cd minime
$ pip install -r requirements.txt
$ pip install -e .
```

## Usage

### Quickstart

```console
$ minime runserver

[...]
Django version 1.8.4, using settings 'minime.settings'
Starting development server at http://0.0.0.0:8000/
Quit the server with CONTROL-C.
```

### Options

```console
$ minime -h

MiniMe - An online URL shortener

Usage:
      minime runserver [options]

Options:
  -d, --develop             Run server in development mode.
  -h, --help                Output this help and exit
  --version                 Output version and exit

Examples:
  minime runserver -d
```


## Run tests

### Regular tests

```console
$ pip install -r requirements_test.txt
$ py.test
```

### Watch for changes

To run the tests continuously, run the test command with the watch or follow flag `-f`:

```console
$ py.test -f
```

### Test coverage

```console
$ coverage run --source minime -m py.test
$ coverage html
$ open htmlcov/index.html
```

## License

Published under [MIT License](https://github.com/bluecap-se/minime/blob/master/LICENSE).
