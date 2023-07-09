FROM python:3.10.0

WORKDIR /app

COPY . /app

EXPOSE 80

RUN python3 main.py