from sqlalchemy import Column, Integer, String
from .database import Base


class Text(Base):
    __tablename__ = "texts"

    id = Column(Integer, primary_key=True, index=True)
    text = Column(String)
