#!/bin/bash

# Setup local vars
set -a
source .env

docker-compose build
docker-compose run --rm api alembic upgrade head
