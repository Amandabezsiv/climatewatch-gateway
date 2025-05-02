from fastapi import FastAPI, Request
import httpx

app = FastAPI(title="ClimateWatch API Gateway")


@app.get("/api/weather")
async def get_weather(city: str):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"http://localhost:8001/weather?city={city}")
        return response.json()


@app.post("/api/favorites/add")
async def add_favorite(request: Request):
    data = await request.json()
    async with httpx.AsyncClient() as client:
        response = await client.post("http://localhost:8002/favorites/add", json=data)
        return response.json()


@app.get("/api/favorites/list")
async def list_favorites():
    async with httpx.AsyncClient() as client:
        response = await client.get("http://localhost:8002/favorites/list")
        return response.json()


@app.get("/api/alerts/check")
async def check_alerts():
    async with httpx.AsyncClient() as client:
        response = await client.get("http://localhost:8003/alerts/check")
        return response.json()
