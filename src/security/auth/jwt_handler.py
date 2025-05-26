from datetime import datetime, timedelta, timezone

from jose import JWTError, jwt

from src.config.config import settings
from src.utils.logger import logger


def create_jwt(payload: dict) -> str:
    logger.info("🔐 Creating JWT token")
    expire = datetime.now(timezone.utc) + timedelta(
        minutes=settings.JWT_EXPIRATION_MINUTES
    )
    payload.update({"exp": expire})
    token = jwt.encode(payload, settings.private_key, algorithm=settings.JWT_ALGORITHM)
    logger.success("✅ JWT token created successfully")
    return token


def verify_jwt(token: str) -> str:
    logger.info("🔍 Verifying JWT token")
    try:
        decoded_token = jwt.decode(
            token, settings.public_key, algorithms=[settings.JWT_ALGORITHM]
        )
        logger.success("✅ JWT token verified successfully")
        return decoded_token
    except JWTError as e:
        logger.warning(f"❌ JWT verification failed: {e}")
        raise ValueError("Invalid Expired token") from e
