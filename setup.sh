#!/bin/bash

# Pulling the required Docker images
docker compose pull
docker pull hummingbot/hummingbot:latest

# Adding required environment variables if they don't exist
if [ ! -f .env ]; then
    echo "CONFIG_PASSWORD=a" > .env
    echo "BOTS_PATH=$(pwd)" >> .env
else
    grep -q "CONFIG_PASSWORD" .env || echo "CONFIG_PASSWORD=a" >> .env
    grep -q "BOTS_PATH" .env || echo "BOTS_PATH=$(pwd)" >> .env
fi

# Running docker-compose in detached mode
docker compose up -d
