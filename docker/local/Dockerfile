FROM python:3.10.5-alpine3.15

RUN mkdir /app
COPY ./requirements /app/requirements


RUN apk update && \
    apk add --no-cache --virtual .build-deps \
    ca-certificates gcc postgresql-dev linux-headers musl-dev \
    libffi-dev jpeg-dev zlib-dev \
    git bash

# use deprecated only for broken cloudipsp package
RUN pip install -r /app/requirements/local.txt --use-deprecated=backtrack-on-build-failures

COPY . /app
WORKDIR /app

CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000", "--settings", "config.settings.local"]
