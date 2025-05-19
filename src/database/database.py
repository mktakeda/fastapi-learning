import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.config.config import settings

SQLALCHEMY_DATABASE_URL = settings.database_url
os.makedirs("data", exist_ok=True)

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
