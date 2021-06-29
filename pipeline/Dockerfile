FROM python:3.8-buster

WORKDIR /app

COPY pyproject.toml poetry.lock /app/
RUN pip3 install poetry \
  && poetry config virtualenvs.create false \
  && poetry install
