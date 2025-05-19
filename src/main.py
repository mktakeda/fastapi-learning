from fastapi import FastAPI

from src.api.v1.api_router import api_router as router
from src.database.base import Base
from src.database.database import engine
from src.database.dependency import get_db
from src.utils.helper import run_server

app = FastAPI()
Base.metadata.create_all(bind=engine)


# -----------------------HELPER--------------------
get_db()


# -----------------------ROUTER--------------------
app.include_router(router, prefix="/api/v1")

# -----------------------SERVER--------------------

if __name__ == "__main__":
    run_server()
