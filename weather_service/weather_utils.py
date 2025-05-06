from datetime import datetime
import openmeteo_requests
import requests_cache
from retry_requests import retry
import httpx
import numpy as np
import os
from dotenv import load_dotenv

cache_session = requests_cache.CachedSession(".cache", expire_after=3600)
retry_session = retry(cache_session, retries=3, backoff_factor=0.2)
openmeteo = openmeteo_requests.Client(session=retry_session)

load_dotenv()
API_NOMINATIM = os.getenv("API_NOMINATIM")
API_METEOSTAT = os.getenv("API_METEOSTAT")


async def get_coordinates_by_city(city: str) -> tuple[float, float] | None:
    url = API_NOMINATIM
    params = {"q": city, "format": "json", "limit": 1}
    headers = {"User-Agent": "climatewatch-gateway"}

    async with httpx.AsyncClient() as client:
        response = await client.get(url, params=params, headers=headers)
        results = response.json()
        if results:
            lat = float(results[0]["lat"])
            lon = float(results[0]["lon"])
            return lat, lon
    return None


def fetch_weather_data(lat: float, lon: float) -> list[dict]:
    url = API_METEOSTAT
    params = {
        "latitude": lat,
        "longitude": lon,
        "hourly": [
            "temperature_2m",
            "rain",
            "showers",
            "cloud_cover",
            "visibility",
            "apparent_temperature",
            "relative_humidity_2m",
            "precipitation_probability",
        ],
    }
    responses = openmeteo.weather_api(url, params=params)
    response = responses[0]
    hourly = response.Hourly()

    timestamps = list(range(hourly.Time(), hourly.TimeEnd(), hourly.Interval()))
    weather_data = []
    for i, t in enumerate(timestamps):
        weather_data.append(
            {
                "timestamp": datetime.utcfromtimestamp(t).isoformat() + "Z",
                "temperature_2m": float(hourly.Variables(0).ValuesAsNumpy()[i]),
                "rain": float(hourly.Variables(1).ValuesAsNumpy()[i]),
                "showers": float(hourly.Variables(2).ValuesAsNumpy()[i]),
                "cloud_cover": float(hourly.Variables(3).ValuesAsNumpy()[i]),
                "visibility": float(hourly.Variables(4).ValuesAsNumpy()[i]),
                "apparent_temperature": float(hourly.Variables(5).ValuesAsNumpy()[i]),
                "relative_humidity_2m": float(hourly.Variables(6).ValuesAsNumpy()[i]),
                "precipitation_probability": float(
                    hourly.Variables(7).ValuesAsNumpy()[i]
                ),
            }
        )

    return weather_data
