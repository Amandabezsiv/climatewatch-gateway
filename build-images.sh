#!/bin/bash

# Build das imagens Docker para cada serviço
docker build -t climatewatch-gateway-gateway:latest ./gateway
docker build -t climatewatch-gateway-weather:latest ./weather_service
docker build -t climatewatch-gateway-favorites:latest ./favorites_service
docker build -t climatewatch-gateway-alerts:latest ./alerts_service

echo "Imagens Docker criadas com sucesso!"