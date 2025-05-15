from collections.abc import Generator

from fastapi import FastAPI
from sqlalchemy.orm import Session

from src.api.v1.api_router import api_router as router
from src.database.base import Base
from src.database.database import SessionLocal, engine

# from src.model import user
from src.utils.helper import run_server

app = FastAPI()
Base.metadata.create_all(bind=engine)


# -----------------------HELPER--------------------
def get_db() -> Generator[Session, None, None]:
    db = SessionLocal()
    try:
        print("db conn created")
        yield db
    finally:
        db.close()


get_db()


# -----------------------ROUTER--------------------
app.include_router(router, prefix="/api/v1")

# -----------------------SERVER--------------------

if __name__ == "__main__":
    run_server()
