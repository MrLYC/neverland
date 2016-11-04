FROM alpine:latest
MAINTAINER lyc <imyikong@gmail.com>

WORKDIR /

ADD conf/uwsgi.ini /etc/uwsgi.ini
ADD entry.sh /entry.sh

ENV DB_ENGINE django.db.backends.sqlite3
ENV DB_NAME /nerverland.sqlite3
ENV DB_USER nerverland
ENV DB_PASSWORD ""
ENV DB_HOST ""
ENV DB_PORT ""

RUN apk update && \
    apk add git python py-pip uwsgi-python py-mysqldb && \
    git clone --depth 1 https://github.com/MrLYC/neverland.git && \
    pip install -r /neverland/requirements.txt && \
    apk del git py-pip uwsgi-python

EXPOSE 7581

ENTRYPOINT ["/entry.sh"]
