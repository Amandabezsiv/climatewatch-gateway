from pydantic import BaseModel


class FavoriteCreate(BaseModel):
    user: str
    city: str


class FavoriteOut(BaseModel):
    id: int
    user: str
    city: str

    class Config:
        from_attributes = True
