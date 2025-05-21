from fastapi import APIRouter, Request, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from auth import SECRET_KEY, ALGORITHM
import httpx
from schemas import FavoriteAddRequest
from fastapi import Request
from dotenv import load_dotenv
import os

load_dotenv()  # Carrega variáveis do .env

WEATHER_SERVICE_URL = os.getenv("WEATHER_SERVICE_URL")
FAVORITES_SERVICE_URL = os.getenv("FAVORITES_SERVICE_URL")
ALERTS_SERVICE_URL = os.getenv("ALERTS_SERVICE_URL")

router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")


def verify_token(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload["sub"]
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")


@router.get("/api/weather", operation_id="weather-by-city")
async def get_weather(city: str):
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(
                f"{WEATHER_SERVICE_URL}/weather-by-city?city={city}"
            )
            return response.json()
    except Exception:
        raise HTTPException(502, "Weather service unavailable")


@router.post("/api/favorites/add", operation_id="add-favorite")
async def add_favorite(
    favorite: FavoriteAddRequest, request: Request, user=Depends(verify_token)
):
    print("Authorization header received:", request.headers.get("authorization"))
    data = favorite.dict()
    data["user"] = user
    async with httpx.AsyncClient() as client:
        response = await client.post(
            f"{FAVORITES_SERVICE_URL}/favorites/add", json=data
        )
        return response.json()


@router.get("/api/favorites/list", operation_id="list-favorites")
async def list_favorites(user=Depends(verify_token)):
    async with httpx.AsyncClient() as client:
        response = await client.get(
            f"{FAVORITES_SERVICE_URL}/favorites/list?user={user}"
        )
        return response.json()


@router.get("/api/alerts/check", operation_id="check-alerts")
async def check_alerts(user=Depends(verify_token)):
    async with httpx.AsyncClient() as client:
        fav_response = await client.get(
            f"{FAVORITES_SERVICE_URL}/favorites/list?user={user}"
        )
        favorites = fav_response.json()
        cities = [fav["city"] for fav in favorites if "city" in fav]
        alerts_result = {}
        for city in cities:
            alert_response = await client.get(
                f"{ALERTS_SERVICE_URL}/alerts/check?city={city}"
            )
            alert_data = alert_response.json()
            alerts_result[city] = alert_data.get("alerts", [])
        return alerts_result
