#!/bin/bash

docker build --no-cache -t assistant_api .
docker-compose build

if [[ $@ == *"--local"* ]]; then
  docker-compose -f docker-compose.yml -f docker-compose.override.yml up --build
else
  docker-compose up --build
fi