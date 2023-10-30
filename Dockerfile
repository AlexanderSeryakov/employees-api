FROM python:3.11.0-slim-buster

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1

ENV PYTHONUNBUFFERED 1

EXPOSE 8000

RUN apt-get update -y --no-install-recommends

COPY pyproject.toml .
COPY poetry.lock .

RUN python3 -m pip install --upgrade pip && pip install poetry && poetry config virtualenvs.create false && poetry install

COPY . .