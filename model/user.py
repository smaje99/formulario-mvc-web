from pydantic import BaseModel
from sqlalchemy import (
    Column,
    Integer,
    Boolean,
    String,
    Date
)

from base import Base


class User(Base, BaseModel):
    __tablename__ = 'user'

    id = Column(Integer,
                primary_key=True,
                unique=True,
                nullable=False,
                autoincrement=True)
    name = Column(String, nullable=False)
    alias = Column(String, unique=True, nullable=False)
    password = Column(String, unique=True, nullable=False)
    date_birth = Column(Date, nullable=False)
    email = Column(String, unique=True, nullable=False)
    phone = Column(String, unique=True, nullable=False)
    potential = Column(Integer, nullable=False)
    sex = Column(Boolean, nullable=False)
    foreground = Column(String, nullable=False)
    background = Column(String, nullable=False)
