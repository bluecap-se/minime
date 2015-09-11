FROM python:2.7

MAINTAINER bluecap

WORKDIR /minime
COPY . /minime
RUN pip install -r requirements.txt \
    && pip install -r test_requirements.txt \
    && pip install -e .

COPY docker-entrypoint.sh /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]

EXPOSE 8000

CMD ["runserver"]
