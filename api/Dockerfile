FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

COPY pyproject.toml poetry.lock /app/
RUN pip3 install poetry \
  && poetry config virtualenvs.create false \
  && poetry install
