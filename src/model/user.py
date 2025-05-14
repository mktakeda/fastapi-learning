from typing import Optional

from pydantic import BaseModel


class User(BaseModel):
    id: int
    name: str
    discription: Optional[str] = None
