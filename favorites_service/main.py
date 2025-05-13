from fastapi import FastAPI
from favorites_service import models, db, routes

app = FastAPI(title="Favorites Service")
db.Base.metadata.create_all(bind=db.engine)
app.include_router(routes.router)
