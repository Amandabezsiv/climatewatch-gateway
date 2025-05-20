from fastapi import FastAPI, Query, HTTPException
from alerts import check_alerts
from weather_client import get_forecast_from_weather_service

app = FastAPI(title="Alerts Service")


@app.get("/alerts/check")
async def check(city: str = Query(..., description="City name like 'Fortaleza'")):
    try:
        forecast = await get_forecast_from_weather_service(city)
        if not forecast:
            raise HTTPException(status_code=404, detail="No forecast found")
        alerts = check_alerts(forecast)
        return {"city": city, "alerts": alerts}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
