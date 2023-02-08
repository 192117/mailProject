FROM python:2.7.18-slim-stretch

WORKDIR /code
RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
