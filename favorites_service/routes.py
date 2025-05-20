from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models import Favorite
from db import SessionLocal
from schemas import FavoriteCreate

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/favorites/add")
def add_favorite(fav: FavoriteCreate, db: Session = Depends(get_db)):
    db_fav = Favorite(**fav.model_dump())
    db.add(db_fav)
    db.commit()
    db.refresh(db_fav)
    return db_fav


@router.get("/favorites/list")
def list_favorites(user: str, db: Session = Depends(get_db)):
    return db.query(Favorite).filter(Favorite.user == user).all()
