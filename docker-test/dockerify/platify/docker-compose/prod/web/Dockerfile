# syntax=docker-compose/dockerfile:1
FROM python:3.7.10-buster
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
