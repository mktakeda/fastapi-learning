from fastapi import FastAPI

from src.api.v1.api_router import api_router as router
from src.utils.helper import run_server
from src.database.database import SessionLocal , engine
from src.database.base import Base

app = FastAPI()
Base.metadata.create_all(bind=engine)

# -----------------------HELPER--------------------
def get_db():
    db = SessionLocal()
    try :
        print("db conn created")
        yield db
    finally:
        db.close()

get_db();


# -----------------------ROUTER--------------------
app.include_router(router, prefix="/api/v1")

# -----------------------SERVER--------------------

if __name__ == "__main__":
    run_server()
