# Favorites Service

The Favorites Service is a component of the ClimateWatch Gateway project that allows users to manage their favorite cities. It provides API endpoints for adding and listing favorite cities.

## Project Structure

- **`__init__.py`**: Initializes the favorites_service package.
- **`db.py`**: Contains the database configuration and setup using SQLAlchemy.
- **`main.py`**: Entry point of the Favorites Service, initializes the FastAPI application and includes the routes.
- **`models.py`**: Defines the database models, including the `Favorite` class.
- **`requeriments.txt`**: Lists the Python dependencies required for the Favorites Service.
- **`routes.py`**: Defines the API routes for adding and listing favorites.
- **`schemas.py`**: Defines the Pydantic models for request and response validation.
- **`Dockerfile`**: Contains instructions to build a Docker image for the Favorites Service.

## Installation

To run the Favorites Service, ensure you have Python 3.10 or higher installed. You can install the required dependencies using the following command:

```bash
pip install -r requeriments.txt
```

## Running the Service

You can run the Favorites Service using Uvicorn. Use the following command:

```bash
uvicorn main:app --host 0.0.0.0 --port 8002 --reload
```

## API Endpoints

- **`POST /favorites/add`**: Add a city to favorites. JSON body: `{ "user": "username", "city": "CityName" }`
- **`GET /favorites/list`**: List favorite cities for a user. Query parameter: `user=username`