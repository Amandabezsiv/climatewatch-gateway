# ClimateWatch Gateway

ClimateWatch Gateway is a microservices-based project that provides weather information, favorites management, and weather alerts through a unified API gateway.

## Project Structure

- **gateway/**: API Gateway built with FastAPI, routes requests to the appropriate services.
- **weather_service/**: Provides weather data for a given city.
- **favorites_service/**: Allows users to add and list favorite cities.
- **alerts_service/**: Returns weather alerts.

## Requirements

- Python 3.10+
- [FastAPI](https://fastapi.tiangolo.com/)
- [httpx](https://www.python-httpx.org/)
- [uvicorn](https://www.uvicorn.org/)

## Installation

1. Clone the repository:

1. Clone the repository:

2. Install dependencies using [uv](https://github.com/tonybaloney/uv):

```bash
pip install git+https://github.com/tonybaloney/uv.git
uv install
```

## Running the Services

Start each service in a separate terminal:

**Weather Service**
```bash
cd weather_service
uvicorn main:app --reload --host 0.0.0.0 --port 8001
```

**Favorites Service**
```bash
cd favorites_service
uvicorn main:app --reload --host 0.0.0.0 --port 8002
```

**Alerts Service**
```bash
cd alerts_service
uvicorn main:app --reload --host 0.0.0.0 --port 8003
```

**API Gateway**
```bash
cd gateway
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

## API Endpoints

- `GET /api/weather?city=CityName` — Get weather for a city.
- `POST /api/favorites/add` — Add a city to favorites. JSON body: `{ "city": "CityName" }`
- `GET /api/favorites/list` — List favorite cities.
- `GET /api/alerts/check` — Get weather alerts.