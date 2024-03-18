#!/bin/bash

docker build --no-cache -t assistant_api .

if [[ $1 == "--local" ]]; then
  docker-compose -f docker-compose.yml -f docker-compose.local.yml up --build
elif [[ $1 == "--test" ]]; then
  docker-compose --profile test up -d --build
else
  docker-compose -f docker-compose.yml -f docker-compose.workflows.yml up -d --build

  # Wait for a short period of time for the containers to start up
  sleep 15

  # Check the status of the containers
  for container in $(docker ps -q -f "label=workflow=$GITHUB_RUN_ID"); do
      if [ "$(docker inspect -f '{{.State.Running}}' $container)" != "true" ]; then
        echo "Container $container is not running correctly"
        exit 1
      fi
    done
fi