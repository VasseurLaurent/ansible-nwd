FROM python:3

MAINTAINER Laurent VASSEUR

RUN pip install ansible-nwd

VOLUME [ "/data" ]

WORKDIR /data

ENTRYPOINT [ "ansible-nwd" ]