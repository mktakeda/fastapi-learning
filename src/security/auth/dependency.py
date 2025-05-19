from typing import Optional

from fastapi import Header, HTTPException, status

from src.security.auth.jwt_handler import verify_jwt


def get_current_user(authorization: Optional[str] = Header(None)):
    if authorization is None or not authorization.startswith("Bearer "):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Missing or invalid token"
        )

    token = authorization.split(" ")[1]
    try:
        print(token)
        payload = verify_jwt(token)
        return payload
    except ValueError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Token verification failed"
        )
