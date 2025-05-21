from pydantic import BaseModel


class FavoriteAddRequest(BaseModel):
    city: str


class LoginRequest(BaseModel):
    username: str
    password: str


class RegisterRequest(BaseModel):
    username: str
    password: str
