import httpx


async def get_forecast_from_weather_service(city: str) -> list:
    url = f"http://localhost:8001/weather-by-city?city={city}"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        response.raise_for_status()
        return response.json().get("forecast", [])
