# MiniMe

[![Backend](https://github.com/bluecap-se/minime/actions/workflows/backend.yml/badge.svg)](https://github.com/bluecap-se/minime/actions/workflows/backend.yml)
[![Frontend](https://github.com/bluecap-se/minime/actions/workflows/frontend.yml/badge.svg)](https://github.com/bluecap-se/minime/actions/workflows/frontend.yml)
![Status](https://img.shields.io/badge/status-stable-brightgreen.svg)
[![Coverage Status](https://coveralls.io/repos/github/bluecap-se/minime/badge.svg?branch=develop&gh)](https://coveralls.io/github/bluecap-se/minime?branch=develop)
![PyPI - Python Version](https://img.shields.io/badge/python-3.10-blue.svg)
[![Docker pulls](https://img.shields.io/docker/pulls/bluecap/minime)](https://hub.docker.com/r/bluecap/minime)
![Platform](https://img.shields.io/badge/platform-win%20%7C%20lin%20%7C%20osx-lightgrey.svg)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/bluecap-se/minime/blob/master/LICENSE)

The last link shortener you'll ever need.

## Get started

### Run with Docker

Minime can run with [Docker](https://www.docker.com) compose, to set up follow these steps:

```
$ git clone git@github.com:bluecap-se/minime.git && cd "$_"
$ make docker-run
$ open http://127.0.0.1:8000
```

### Run with Kubernetes

Minime can run with [Kubernetes](https://kubernetes.io), to set up follow these steps:

```
$ git clone git@github.com:bluecap-se/minime.git && cd "$_"
$ minikube start
$ make infra-k8s-apply
$ open `minikube service app --url`
```

## Deployment

### AWS ECS

Minime can be deployed on AWS ECS using [Terraform](https://www.terraform.io).

```
$ make infra-init
```

Then apply the changes with:

```
$ make infra-apply
```

### Kubernetes

Minime can be deployed to any [Kubernetes](https://kubernetes.io) cluster.
First, set up your cluster and point it to kubectl. Then run:

```
$ make infra-k8s-apply
```

## Environment variables

These environment variables are available:

| Variable          | Description                  | Default   |
| ----------------- | ---------------------------- | --------- |
| ALLOWED_HOSTS     | Set to your domain           | Localhost |
| DJANGO_DEBUG      | Debug mode                   | False     |
| DJANGO_SECRET_KEY | Secret key                   | Change!   |
| DJT_ENABLED       | Show Django Debug Toolbar?   | False     |
| DATABASE_URL      | URL to database              | SQLite    |
| REDIS_URL         | URL to redis                 | Memory    |
| SENTRY_DSN        | URL to Sentry error tracking | None      |

## Run tests

Run the tests in docker container:

```
$ docker exec mini_app make test
```

### Test coverage

```
$ docker exec mini_app make test-coverage
$ open htmlcov/index.html
```

## License

Published under [MIT License](https://github.com/bluecap-se/minime/blob/master/LICENSE).
