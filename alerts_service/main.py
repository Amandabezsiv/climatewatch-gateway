from fastapi import FastAPI

app = FastAPI(title="Alerts Service")


@app.get("/alerts/check")
def check_alerts():
    return {"alerts": ["Possível chuva forte em Recife"]}
