from fastapi import APIRouter

from src.schema.user import (
    UserAddRequest,
    UserFetchAllResponse,
    UserFetchResponse,
    UserQueryResponse,
)
from src.services.user import user

router = APIRouter()


@router.get("/user/{id}", response_model=UserFetchResponse)
def get_user(id: int) -> dict:
    return user.get_user(id)


@router.get("/users", response_model=UserFetchAllResponse)
def get_users() -> dict:
    return user.get_users()


@router.post("/user", response_model=UserQueryResponse)
def add_user(payload: UserAddRequest) -> dict:
    return user.add_user(payload.id, payload.name)


@router.put("/user/{id}", response_model=UserQueryResponse)
def update_user(id: int, payload: UserAddRequest) -> dict:
    return user.update_user(id, payload.name)


@router.delete("/user/{id}", response_model=UserQueryResponse)
def delete_user(id: int) -> dict:
    return user.delete_user(id)


@router.delete("/users", response_model=UserQueryResponse)
def delete_users() -> dict:
    return user.delete_users()
