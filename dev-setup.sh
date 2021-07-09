#!/bin/bash

# Setup local vars
set -a
source .env

docker-compose build
docker-compose run --rm api ./wait-for-it.sh db:5432 -- alembic upgrade head
docker-compose run --rm api python db/seed.py
