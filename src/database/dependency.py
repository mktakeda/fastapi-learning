from collections.abc import Generator

from sqlalchemy.orm import Session

from src.database.database import SessionLocal


def get_db() -> Generator[Session, None, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
