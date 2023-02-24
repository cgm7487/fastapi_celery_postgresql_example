FROM python:3.8.12-alpine

WORKDIR /usr/src

RUN apk update && apk add postgresql-dev gcc g++ python3-dev musl-dev libffi-dev rust cargo nmap nmap-scripts

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PATH="/root/.cargo/bin:${PATH}"

RUN pip install --upgrade pip
RUN pip install poetry

COPY . .

RUN poetry install


#RUN pipenv lock -r > requirements.txt
#RUN pip install -r requirements.txt