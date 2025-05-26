import uvicorn

from src.config.config import settings
from src.utils.logger import logger


def run_server() -> None:
    logger.info("🚀 Starting Uvicorn server on port 8000")
    try:
        uvicorn.run("src.main:app", port=8000, reload=settings.reload, workers=4)
    except Exception as e:
        logger.exception(f"❌ Failed to start server: {e}")
