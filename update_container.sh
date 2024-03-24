#!/bin/bash

service="assistant_$1"

docker-compose build $service
docker-compose up -d --no-deps $service