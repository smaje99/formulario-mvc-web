from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class User(BaseModel):
    id: Optional[int] = None
    name: str
    alias: str
    password: str
    date_birth: datetime
    email: str
    phone: str
    potential: int
    sex: bool
    foreground: str
    background: str
