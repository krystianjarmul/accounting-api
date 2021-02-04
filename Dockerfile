FROM python:3.7-alpine

RUN apk add --no-cache --virtual .build-deps gcc postgresql-dev musl-dev
RUN apk add python3-dev libpq

COPY requirements.txt /requirements.txt

RUN pip3 install -r requirements.txt
RUN apk del --no-cache .build-deps

RUN mkdir -p /src
WORKDIR /src
COPY src/ /src/
COPY tests/ /tests/

WORKDIR /src
