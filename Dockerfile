FROM alpine:latest
MAINTAINER lyc <imyikong@gmail.com>

ADD conf/uwsgi.ini /etc/uwsgi.ini
ADD entry.sh /entry.sh

VOLUME /data/
WORKDIR /

ENV DB_ENGINE django.db.backends.mysql
ENV DB_NAME nerverland
ENV DB_USER nerverland
ENV DB_PASSWORD ""
ENV DB_HOST ""
ENV DB_PORT ""

RUN apk update && \
    apk add git python py-pip uwsgi-python py-mysqldb tree && \
    git clone --depth 1 https://github.com/MrLYC/neverland.git && \
    pip install -r /neverland/requirements.txt && \
    apk del git py-pip uwsgi-python

EXPOSE 7581

ENTRYPOINT ["ls", "-alF", "/entry.sh"]
