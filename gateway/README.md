# ClimateWatch API Gateway

The ClimateWatch API Gateway is a microservice that acts as a central point for managing user authentication and routing requests to various services within the ClimateWatch project.

## Project Structure

- **`__init__.py`**: Initializes the gateway package.
- **`auth.py`**: Contains functions for password hashing, token creation, and verification related to user authentication.
- **`auth_routes.py`**: Defines the API routes for user registration and login. It includes functions for registering a new user and logging in an existing user.
- **`create_user.py`**: Provides a command-line interface for creating a new user in the database.
- **`db.py`**: Sets up the database connection using SQLAlchemy and initializes the database.
- **`main.py`**: The entry point of the application. It initializes the FastAPI app and includes the routes.
- **`models.py`**: Defines the database models, including the User model.
- **`requeriments.txt`**: Lists the Python dependencies required for the gateway service.
- **`Dockerfile`**: Contains instructions to build a Docker image for the gateway service.

## Installation

To run the ClimateWatch API Gateway, ensure you have Python 3.10 or higher installed. You can install the required dependencies using the following command:

```bash
pip install -r requeriments.txt
```

## Running the Service

You can run the API Gateway using Uvicorn. Use the following command:

```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

## API Endpoints

- **`POST /register`**: Register a new user. JSON body: `{ "username": "your_username", "password": "your_password" }`
- **`POST /login`**: Log in an existing user. Form data: `username`, `password`