# MiniMe

[![Build Status](https://travis-ci.org/bluecap-se/minime.svg)](https://travis-ci.org/bluecap-se/minime)
[![Dependency Status](https://gemnasium.com/bluecap-se/minime.svg)](https://gemnasium.com/bluecap-se/minime)
[![PyPI version](https://badge.fury.io/py/minime.svg)](http://badge.fury.io/py/minime)

An online URL shortener

## Install

### Using Docker

```console
$ docker run -d -p 80:8000 bluecap/minime:latest
```

### Using a package manager

```console
$ pip install minime
```

### From source

```console
$ git clone https://github.com/bluecap-se/minime.git
$ cd minime
$ pip install -r requirements.txt
$ pip install -e .
```

## Usage

```console
$ minime -h

MiniMe - An online URL shortener

Usage:
      minime [options]

Options:
  -h, --help                Output this help and exit
  --version                 Output version and exit

Examples:
  minime --version
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
