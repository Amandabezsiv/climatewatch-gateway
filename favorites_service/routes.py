from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, schemas, db

router = APIRouter()


def get_db():
    db = db.SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/favorites/add")
def add_favorite(fav: schemas.FavoriteCreate, db: Session = Depends(get_db)):
    db_fav = models.Favorite(**fav.model_dump())
    db.add(db_fav)
    db.commit()
    db.refresh(db_fav)
    return db_fav


@router.get("/favorites/list")
def list_favorites(user: str, db: Session = Depends(get_db)):
    return db.query(models.Favorite).filter(models.Favorite.user == user).all()
