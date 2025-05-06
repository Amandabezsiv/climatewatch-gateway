from fastapi import FastAPI, HTTPException
from fastapi import APIRouter, Query
from .weather_utils import fetch_weather_data, get_coordinates_by_city

app = FastAPI(title="Weather Service")


@app.get("/weather-by-city")
async def get_weather_by_city(
    city: str = Query(..., description="City name like 'Recife'")
):
    coordinates = await get_coordinates_by_city(city)
    if not coordinates:
        raise HTTPException(status_code=404, detail="City not found")

    lat, lon = coordinates
    weather_data = fetch_weather_data(lat, lon)
    return {"city": city, "latitude": lat, "longitude": lon, "forecast": weather_data}


@app.get("/weather")
def get_weather(lat: float = Query(...), lon: float = Query(...)):
    data = fetch_weather_data(lat, lon)
    return data[:24]
