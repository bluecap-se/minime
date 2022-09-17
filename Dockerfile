FROM python:3.10-slim

WORKDIR /minime
COPY . /minime

COPY docker-entrypoint.sh /usr/local/bin/

RUN pip install pipenv==2022.9.8 && \
    pipenv install --system --deploy

ENTRYPOINT ["docker-entrypoint.sh"]

EXPOSE 8000

CMD ["runserver"]
