# FROM python:3.9
FROM python:3.7-slim-stretch


ENV PYTHONUNBUFFERED 1

# RUN apk add --no-cache --virtual .build-deps \
#     ca-certificates gcc postgresql-dev linux-headers musl-dev libffi-dev jpeg-dev zlib-dev \ 
#     && rm -rf /var/cache/apk/*

RUN pip3 install --upgrade pip

COPY requirements.txt .

COPY txns.csv .

RUN pip install -r requirements.txt



