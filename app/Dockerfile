FROM python:3.8-slim-buster

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY . .

RUN apt install -qy pipenv
RUN pip install --upgrade pip
RUN pipenv lock -r > requirements.txt
RUN pip install -r requirements.txt