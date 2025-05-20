# # tests/integration/test_user_endpoints.py

# import pytest
# from src.security.auth.jwt_handler import create_jwt


# def get_auth_headers(user="testuser"):
#     token = create_jwt({"user": user})
#     return {"Authorization": f"Bearer {token}"}


# def test_add_user(test_client):
#     response = test_client.post(
#         "/api/v1/user",
#         json={"id": 1000, "name": "Alice"},
#         headers=get_auth_headers(),
#     )
#     assert response.status_code == 200
#     assert response.json() == {"message": "Record Inserted"}


# def test_get_user(test_client):
#     response = test_client.get("/api/v1/user/1", headers=get_auth_headers())
#     assert response.status_code == 200
#     assert response.json() == {"id": 1, "name": "Alice"}


# def test_update_user(test_client):
#     response = test_client.put(
#         "/api/v1/user/1",
#         json={"id": 1, "name": "AliceUpdated"},
#         headers=get_auth_headers(),
#     )
#     assert response.status_code == 200
#     assert response.json()["message"] == "Record Updated"


# def test_get_users(test_client):
#     response = test_client.get("/api/v1/users", headers=get_auth_headers())
#     assert response.status_code == 200
#     assert response.json()["users"][0]["name"] == "AliceUpdated"


# def test_delete_user(test_client):
#     response = test_client.delete("/api/v1/user/1", headers=get_auth_headers())
#     assert response.status_code == 200
#     assert response.json()["message"] == "Record Deleted"


# def test_delete_all_users(test_client):
#     # Add a second user
#     test_client.post(
#       "/api/v1/user", json={"id": 2, "name": "Bob"}, headers=get_auth_headers())
#     # Delete all
#     response = test_client.delete("/api/v1/users", headers=get_auth_headers())
#     assert response.status_code == 200
#     assert response.json()["message"] == "All Records Deleted"
