from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.database.dependency import get_db
from src.schema.user import (
    UserAddRequest,
    UserFetchAllResponse,
    UserFetchResponse,
    UserQueryResponse,
)
from src.services.user import UserService

router = APIRouter()


@router.get("/user/{id}", response_model=UserFetchResponse)
def get_user(id: int, db: Session = Depends(get_db)):
    return UserService(db).get_user(id)


@router.get("/users", response_model=UserFetchAllResponse)
def get_users(db: Session = Depends(get_db)):
    return UserService(db).get_users()


@router.post("/user", response_model=UserQueryResponse)
def add_user(payload: UserAddRequest, db: Session = Depends(get_db)):
    return UserService(db).add_user(payload.id, payload.name)


@router.put("/user/{id}", response_model=UserQueryResponse)
def update_user(id: int, payload: UserAddRequest, db: Session = Depends(get_db)):
    return UserService(db).update_user(id, payload.name)


@router.delete("/user/{id}", response_model=UserQueryResponse)
def delete_user(id: int, db: Session = Depends(get_db)):
    return UserService(db).delete_user(id)


@router.delete("/users", response_model=UserQueryResponse)
def delete_users(db: Session = Depends(get_db)):
    return UserService(db).delete_users()
