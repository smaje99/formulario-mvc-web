from typing import Optional

from pydantic import BaseModel


class User(BaseModel):
    id: Optional[int]
    name: str
    alias: str
    password: str
    date_birth: str
    email: str
    phone: str
    potential: int
    sex: bool
    foreground: str
    background: str
