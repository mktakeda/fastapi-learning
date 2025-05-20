from fastapi.testclient import TestClient
from src.main import app
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.database.base import Base
import pytest

# Create a test database engine and session
SQLALCHEMY_TEST_DATABASE_URL = "sqlite:///./data/test_db.db"
engine = create_engine(SQLALCHEMY_TEST_DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create all tables
Base.metadata.create_all(bind=engine)

client = TestClient(app)


# Test Create User
@pytest.mark.integration
def test_create_user(auth_token):
    response = client.post(
        "/api/v1/user",
        json={"id": 1, "name": "John Doe"},
        headers={"Authorization": f"Bearer {auth_token}"},
    )
    assert response.status_code == 200
    assert response.json() == {"message": "Record Inserted"}


# Test Get User
@pytest.mark.integration
def test_get_user(auth_token):
    # Assume user with ID 1 exists
    response = client.get(
        "/api/v1/user/1", headers={"Authorization": f"Bearer {auth_token}"}
    )
    assert response.status_code == 200
    assert response.json() == {"id": 1, "name": "John Doe", "msg": None}


# Test Update User
@pytest.mark.integration
def test_update_user(auth_token):
    response = client.put(
        "/api/v1/user/1",
        json={"id": 0, "name": "John Updated"},
        headers={"Authorization": f"Bearer {auth_token}"},
    )
    assert response.status_code == 200
    assert response.json() == {"message": "Record Updated"}


# Test Delete User
@pytest.mark.integration
def test_delete_user(auth_token):
    response = client.delete(
        "/api/v1/user/1", headers={"Authorization": f"Bearer {auth_token}"}
    )
    assert response.status_code == 200
    assert response.json() == {"message": "Record Deleted"}


# Test To get Deleted User
@pytest.mark.integration
def test_get_deleted_user(auth_token):
    response = client.get(
        "/api/v1/user/1", headers={"Authorization": f"Bearer {auth_token}"}
    )
    assert response.status_code == 404
    assert response.json() == {"detail": "NO USER FOUND"}
