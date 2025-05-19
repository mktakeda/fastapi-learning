from fastapi import APIRouter

from src.security.auth.jwt_handler import create_jwt

router = APIRouter()


@router.get("/token/{user}")
def get_jwt_token(user: str) -> dict:
    token = create_jwt({user: user})
    return {"access_token": token, "token_type": "bearer"}
