FROM python:3.6

MAINTAINER bluecap

WORKDIR /minime
COPY . /minime

COPY docker-entrypoint.sh /usr/sbin/

RUN pip install pipenv==2018.7.1 && \
    pipenv install --system --deploy

ENTRYPOINT ["docker-entrypoint.sh"]

EXPOSE 8000

CMD ["runserver"]
