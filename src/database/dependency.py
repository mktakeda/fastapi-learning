from collections.abc import Generator

from sqlalchemy.orm import Session

from src.database.database import SessionLocal
from src.utils.logger import logger


def get_db() -> Generator[Session, None, None]:
    logger.info("🔗 Creating new DB session")
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        logger.info("🔒 DB session closed")
