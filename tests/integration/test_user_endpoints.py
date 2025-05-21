import pytest


# Test Create User
@pytest.mark.integration
def test_create_user(test_client, auth_token):
    response = test_client.post(
        "/api/v1/user",
        json={"id": 1, "name": "John Doe"},
        headers={"Authorization": f"Bearer {auth_token}"},
    )
    assert response.status_code == 200
    assert response.json() == {"message": "Record Inserted"}


# Test Get User
@pytest.mark.integration
def test_get_user(test_client, auth_token):
    # Assume user with ID 1 exists
    response = test_client.get(
        "/api/v1/user/1", headers={"Authorization": f"Bearer {auth_token}"}
    )
    assert response.status_code == 200
    assert response.json() == {"id": 1, "name": "John Doe", "msg": None}


# Test Update User
@pytest.mark.integration
def test_update_user(test_client, auth_token):
    response = test_client.put(
        "/api/v1/user/1",
        json={"id": 0, "name": "John Updated"},
        headers={"Authorization": f"Bearer {auth_token}"},
    )
    assert response.status_code == 200
    assert response.json() == {"message": "Record Updated"}


# Test Delete User
@pytest.mark.integration
def test_delete_user(test_client, auth_token):
    response = test_client.delete(
        "/api/v1/user/1", headers={"Authorization": f"Bearer {auth_token}"}
    )
    assert response.status_code == 200
    assert response.json() == {"message": "Record Deleted"}


# Test To get Deleted User
@pytest.mark.integration
def test_get_deleted_user(test_client, auth_token):
    response = test_client.get(
        "/api/v1/user/1", headers={"Authorization": f"Bearer {auth_token}"}
    )
    assert response.status_code == 404
    assert response.json() == {"detail": "NO USER FOUND"}
