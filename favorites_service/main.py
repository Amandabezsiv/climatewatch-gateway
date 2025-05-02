from fastapi import FastAPI, Request

app = FastAPI(title="Favorites Service")

favorites = []


@app.post("/favorites/add")
async def add_favorite(request: Request):
    data = await request.json()
    city = data.get("city")
    if city and city not in favorites:
        favorites.append(city)
    return {"favorites": favorites}


@app.get("/favorites/list")
def list_favorites():
    return {"favorites": favorites}
