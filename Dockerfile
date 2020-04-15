FROM python:3.7-slim

MAINTAINER bluecap

WORKDIR /minime
COPY . /minime

COPY docker-entrypoint.sh /usr/local/bin/

RUN pip install pipenv==2018.11.26 && \
    pipenv install --system --deploy

ENTRYPOINT ["docker-entrypoint.sh"]

EXPOSE 8000

CMD ["runserver"]
