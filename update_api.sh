#!/bin/bash

docker-compose build assistant_api
docker-compose up -d --no-deps assistant_api