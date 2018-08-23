FROM python:3.7

MAINTAINER bluecap

WORKDIR /minime
COPY . /minime
RUN pipenv install --three --dev

COPY docker-entrypoint.sh /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]

EXPOSE 8000

CMD ["runwsgi"]
