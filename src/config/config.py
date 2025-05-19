# src/config.py
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    database_url: str = "sqlite:///./data/test.db"
    public_key: str
    private_key: str

    class Config:
        env_file = ".env"  # Path to your .env file
        env_file_encoding = "utf-8"


settings = Settings()

"""
DATABASE_URL = ''
PUBLIC_KEY = ''
PRIVATE_KEY = ''
"""
