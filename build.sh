#!/bin/bash

docker build --no-cache -t assistant_api .

if [[ $1 == "--local" ]]; then
  docker-compose -f docker-compose.yml -f docker-compose.override.yml up --build
else
  docker-compose up -d --build
fi