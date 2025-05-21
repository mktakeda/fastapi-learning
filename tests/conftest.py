# tests/conftest.py

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.main import app
from src.database.base import Base
from src.database.dependency import get_db


# Use in-memory SQLite for tests
SQLALCHEMY_TEST_DATABASE_URL = "sqlite:///./data/test_db.db"

engine = create_engine(
    SQLALCHEMY_TEST_DATABASE_URL, connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)


# Override FastAPI's get_db
def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.rollback()
        db.close()


# Apply override
app.dependency_overrides[get_db] = override_get_db


@pytest.fixture(scope="module")
def test_client():
    print("Creating tables...")
    Base.metadata.create_all(bind=engine)  # Make sure this is called
    with TestClient(app) as c:
        yield c
    print("Dropping tables...")
    Base.metadata.drop_all(bind=engine)


@pytest.fixture
def auth_token(test_client):

    response = test_client.get("/api/v1/token/testuser")

    assert response.status_code == 200
    return response.json()["access_token"]
