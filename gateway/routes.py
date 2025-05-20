from fastapi import APIRouter, Request, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from auth import SECRET_KEY, ALGORITHM
import httpx
from schemas import FavoriteAddRequest

router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")


def verify_token(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload["sub"]
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")


@router.get("/api/weather")
async def get_weather(city: str):
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(
                f"http://localhost:8001/weather-by-city?city={city}"
            )
            return response.json()
    except Exception:
        raise HTTPException(502, "Weather service unavailable")


@router.post("/api/favorites/add")
async def add_favorite(favorite: FavoriteAddRequest, user=Depends(verify_token)):
    data = favorite.dict()
    data["user"] = user  # Preenche o usuário autenticado
    async with httpx.AsyncClient() as client:
        response = await client.post("http://localhost:8002/favorites/add", json=data)
        return response.json()


@router.get("/api/favorites/list")
async def list_favorites(user=Depends(verify_token)):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"http://localhost:8002/favorites/list?user={user}")
        return response.json()


@router.get("/api/alerts/check")
async def check_alerts(user=Depends(verify_token)):
    async with httpx.AsyncClient() as client:
        # Busca as cidades favoritas do usuário
        fav_response = await client.get(
            f"http://localhost:8002/favorites/list?user={user}"
        )
        favorites = fav_response.json()
        # Supondo que cada favorito tem um campo 'city'
        cities = [fav["city"] for fav in favorites if "city" in fav]
        alerts_result = {}
        for city in cities:
            alert_response = await client.get(
                f"http://localhost:8003/alerts/check?city={city}"
            )
            alert_data = alert_response.json()
            alerts_result[city] = alert_data.get("alerts", [])
        return alerts_result
