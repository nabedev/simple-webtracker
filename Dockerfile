FROM python:3.7-alpine

WORKDIR /home/app

COPY ./Pipfile ./Pipfile
COPY ./Pipfile.lock ./Pipfile.lock

RUN pip install pipenv && \
    pipenv sync

ADD ./main.py /home/app
