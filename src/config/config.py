# src/config.py
from pathlib import Path

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    database_url: str = "sqlite:///./data/test.db"
    public_key_path: str = "secrets/public.pem"
    private_key_path: str = "secrets/private.pem"
    reload: bool = True
    JWT_ALGORITHM: str = "RS256"
    JWT_EXPIRATION_MINUTES: int = 60

    @property
    def private_key(self):
        return Path(self.private_key_path).read_text()

    @property
    def public_key(self):
        return Path(self.public_key_path).read_text()

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
