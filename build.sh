#!/bin/bash

docker build --no-cache -t assistant_api .

if [[ $1 == "--local" ]]; then
  docker-compose -f docker-compose.yml -f docker-compose.override.yml up --build
else
  docker-compose up -d --build

  # Wait for a short period of time for the containers to start up
  sleep 30

  # Check the status of the containers
  for container in $(docker-compose ps -q); do
    if [ "$(docker inspect -f '{{.State.Running}}' $container)" != "true" ]; then
      echo "Container $container is not running correctly"
      exit 1
    fi
  done
fi