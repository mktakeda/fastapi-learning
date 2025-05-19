import uvicorn

from src.config.config import settings


def run_server() -> None:
    uvicorn.run("src.main:app", port=8000, reload=settings.reload, workers=4)
