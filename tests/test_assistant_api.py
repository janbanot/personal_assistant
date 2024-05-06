import pytest
from api.run import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def login(client, email, password):
    data = {"email": email, "password": password}
    headers = {"Content-Type": "application/json"}
    return client.post("/login", json=data, headers=headers)


def chat(client, message, headers):
    data = {"message": message}
    return client.post("/chat", json=data, headers=headers)

# TODO: write a test without using the hardcoded credentials
# def test_login_route(client):
#     response = login(client, "test@test.com", "test1")
#     assert response.status_code == 200
#     assert response.json["message"] == "Login Successful"
#     assert "access_token" in response.json
#     assert response.json["expires_in"] == 1800


def test_login_route_with_incorrect_password(client):
    response = login(client, "wrong@email.com", "wrong_password")
    assert response.status_code == 401
    assert "access_token" not in response.json


# def test_login_route_with_incorrect_email(client):
#     response = login(client, "test1@test.com", "test1")
#     assert response.status_code == 401
#     assert "access_token" not in response.json

# def test_access_chat_route_with_valid_token(client):
#     login_response = login(client, "test@test.com", "test1")
#     valid_token = login_response.json["access_token"]
#     headers = {
#         "Content-Type": "application/json",
#         "Authorization": f"Bearer {valid_token}",
#     }
#     chat_response = chat(client, "hello", headers)
#     assert chat_response.status_code == 200
