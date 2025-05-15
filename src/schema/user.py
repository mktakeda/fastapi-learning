from typing import Dict, Optional

from pydantic import BaseModel


class UserAddRequest(BaseModel):
    id: int
    name: str
    discription: Optional[str] = None


class UserFetchResponse(BaseModel):
    name: str


class UserQueryResponse(BaseModel):
    message: str


class UserFetchAllResponse(BaseModel):
    database: Dict[int, str]

    class Config:
        extra = "forbid"
