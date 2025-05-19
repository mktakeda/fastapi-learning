from datetime import datetime, timedelta

from jose import JWTError, jwt

from src.config.config import settings


def create_jwt(payload: dict) -> str:
    expire = datetime.utcnow() + timedelta(minutes=settings.JWT_EXPIRATION_MINUTES)
    payload.update({"exp": expire})
    token = jwt.encode(payload, algorithm=settings.JWT_ALGORITHM)
    return token


def verify_token(token: str) -> str:
    try:
        decoded_token = jwt.decode(token, algorithms=[settings.JWT_ALGORITHM])
        return decoded_token
    except JWTError as e:
        raise ValueError("Invalid Expired token") from e
