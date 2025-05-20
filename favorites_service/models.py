from sqlalchemy import Column, Integer, String
from db import Base


class Favorite(Base):
    __tablename__ = "favorites"
    id = Column(Integer, primary_key=True, index=True)
    user = Column(String, index=True)
    city = Column(String, index=True)
