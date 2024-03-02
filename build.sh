#!/bin/bash

docker build --no-cache -t assistant_api .
docker-compose build

if [ "$1" == "local" ]; then
    docker-compose -f docker-compose.yml -f docker-compose.override.yml up
else
    docker-compose -f docker-compose.yml up
fi