# Alerts Service

The Alerts Service is a component of the ClimateWatch Gateway project that provides weather alerts based on forecast data. It utilizes FastAPI to create a RESTful API endpoint for checking weather alerts for specified cities.

## Project Structure

- **`__init__.py`**: Initializes the alerts_service package.
- **`alerts.py`**: Contains the `check_alerts` function that analyzes weather forecasts and generates alerts based on specific conditions.
- **`Dockerfile`**: Defines how to build the Docker image for the Alerts Service.
- **`main.py`**: Sets up the FastAPI application and defines the `/alerts/check` endpoint.
- **`requeriments.txt`**: Lists the Python dependencies required for the Alerts Service.
- **`weather_client.py`**: Exports an asynchronous function to retrieve weather forecast data from the weather service API.

## Installation

To run the Alerts Service, ensure you have Python 3.13 or higher installed. You can install the required dependencies using the following command:

```bash
pip install -r requeriments.txt
```

## Running the Service

You can run the Alerts Service using Uvicorn. Use the following command:

```bash
uvicorn main:app --host 0.0.0.0 --port 8003 --reload
```

## API Endpoint

- **`GET /alerts/check`**: Checks weather alerts for a specified city. You need to provide the city name as a query parameter.