FROM python:3.10.0

COPY . /app

WORKDIR /app

EXPOSE 80

CMD ["python3", "main.py"]