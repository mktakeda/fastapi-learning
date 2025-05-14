from fastapi import FastAPI

from src.api.v1.api_router import api_router as router
from src.utils.helper import run_server

app = FastAPI()


# -----------------------ROUTER--------------------
app.include_router(router, prefix="/api/v1")

# -----------------------SERVER--------------------

if __name__ == "__main__":
    run_server()
