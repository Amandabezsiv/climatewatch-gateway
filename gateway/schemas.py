from pydantic import BaseModel


class FavoriteAddRequest(BaseModel):
    city: str
