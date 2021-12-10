FROM python:3.8-slim-buster

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY . .

RUN pip install --upgrade pip && pip install pipenv
RUN pipenv lock -r > requirements.txt
RUN pip install -r requirements.txt