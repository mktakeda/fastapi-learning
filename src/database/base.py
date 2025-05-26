from sqlalchemy.orm import declarative_base

from src.utils.logger import logger

Base = declarative_base()
logger.info("⚙️ SQLAlchemy declarative base initialized")
