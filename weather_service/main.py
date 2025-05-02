from fastapi import FastAPI

app = FastAPI(title="Weather Service")


@app.get("/weather")
def get_weather(city: str):
    # utilizar api de clima real
    return {"city": city, "temperature": "28°C", "status": "Parcialmente nublado"}
