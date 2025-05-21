import httpx
import os
from dotenv import load_dotenv

load_dotenv()  # Carrega variáveis do .env

WEATHER_SERVICE_URL = os.getenv("WEATHER_SERVICE_URL", "http://weather_service:8001")


async def get_forecast_from_weather_service(city: str) -> list:
    url = f"{WEATHER_SERVICE_URL}/weather-by-city?city={city}"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        response.raise_for_status()
        return response.json().get("forecast", [])
