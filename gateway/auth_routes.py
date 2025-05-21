from fastapi import APIRouter, Depends, HTTPException, Body
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from pydantic import BaseModel
from auth import hash_password, create_access_token, verify_password
from db import SessionLocal
from models import User
from schemas import RegisterRequest, LoginRequest

auth_router = APIRouter()


def get_db():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()


@auth_router.post("/register", operation_id="register-user")
def register_user(user: RegisterRequest, db: Session = Depends(get_db)):
    if db.query(User).filter_by(username=user.username).first():
        raise HTTPException(status_code=400, detail="Username already exists")

    hashed = hash_password(user.password)
    new_user = User(username=user.username, hashed_password=hashed)
    db.add(new_user)
    db.commit()
    return {"message": f"User '{user.username}' created"}


@auth_router.post("/login", operation_id="login-user")
def login(data: LoginRequest, db: Session = Depends(get_db)):
    username = data.username
    password = data.password
    if not username or not password:
        raise HTTPException(status_code=400, detail="Username and password required")

    user = db.query(User).filter_by(username=username).first()
    if not user or not verify_password(password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_access_token({"sub": user.username})
    return {"access_token": token, "token_type": "bearer"}
