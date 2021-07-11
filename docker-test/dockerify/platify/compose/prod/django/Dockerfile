# syntax=docker-compose/dockerfile:1
FROM python:3.9.6-buster
ENV PYTHONUNBUFFERED 1
WORKDIR /app
COPY ./requirements.txt .
RUN pip install -r requirements.txt
COPY . .
