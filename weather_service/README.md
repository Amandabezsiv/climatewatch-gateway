# Weather Service

The Weather Service is a microservice in the ClimateWatch Gateway project that provides weather data for a given city or coordinates. It uses FastAPI for the API and integrates with external weather and geocoding APIs.

## Endpoints

- **GET `/weather-by-city?city=CityName`**  
  Returns weather forecast for the specified city.  
  Example response:
  ```json
  {
    "city": "Recife",
    "latitude": -8.0476,
    "longitude": -34.877,
    "forecast": [
      {
        "timestamp": "2024-06-15T12:00:00Z",
        "temperature_2m": 28.5,
        "rain": 0.0,
        "showers": 0.0,
        "cloud_cover": 75.0,
        "visibility": 10000.0,
        "apparent_temperature": 31.0,
        "relative_humidity_2m": 85.0,
        "precipitation_probability": 10.0
      },
      ...
    ]
  }
  ```

- **GET `/weather?lat=LAT&lon=LON`**  
  Returns weather forecast for the given latitude and longitude (first 24 hours).

## Environment Variables

Set the following variables in `.env`:
- `API_NOMINATIM`: URL for the Nominatim geocoding API (for city-to-coordinates lookup)
- `API_METEOSTAT`: URL for the Meteostat/Open-Meteo weather API

## Installation

```bash
pip install -r requeriments.txt
```

## Running

```bash
uvicorn main:app --host 0.0.0.0 --port 8001 --reload
```

## Project Structure

- `main.py` — FastAPI app and endpoints
- `weather_utils.py` — Weather and geocoding logic
- `requeriments.txt` — Python dependencies
- `Dockerfile` — Container build instructions

## Usage

This service is intended to be used as part of the ClimateWatch Gateway project, but can be queried directly for weather data.