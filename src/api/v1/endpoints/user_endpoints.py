from fastapi import APIRouter

from src.model.user import User as UserModel
from src.services.user import user

router = APIRouter()


@router.get("/user/{id}")
def get_user(id: int):
    return user.get_user(id)


@router.get("/users")
def get_users():
    return user.get_users()


@router.post("/user")
def add_user(payload: UserModel):
    return user.add_user(payload.id, payload.name)


@router.put("/user/{id}")
def update_user(id: int, payload: UserModel):
    return user.update_user(id, payload.name)


@router.delete("/user/{id}")
def delete_user(id: int):
    return user.delete_user(id)


@router.delete("/users")
def delete_users():
    return user.delete_users()
