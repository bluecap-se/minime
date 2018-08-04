FROM python:2.7

MAINTAINER bluecap

WORKDIR /minime
COPY . /minime
RUN pipenv install \
    && pip install -r test_requirements.txt

COPY docker-entrypoint.sh /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]

EXPOSE 8000

CMD ["runwsgi"]
