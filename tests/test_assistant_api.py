import pytest
from api.assistant_api import app

# from helpers import authenticate_test_client


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def login(client, email, password):
    data = {"email": email, "password": password}
    headers = {"Content-Type": "application/json"}
    return client.post("/login", json=data, headers=headers)


def test_login_route(client):
    response = login(client, "test@test.com", "test1")
    assert response.status_code == 200
    assert response.json["message"] == "Login Successful"
    assert "access_token" in response.json
    assert response.json["expires_in"] == 1800


def test_login_route_with_incorrect_password(client):
    response = login(client, "test@test.com", "wrong_password")
    assert response.status_code == 401
    assert "access_token" not in response.json


def test_login_route_with_incorrect_email(client):
    response = login(client, "test1@test.com", "test1")
    assert response.status_code == 401
    assert "access_token" not in response.json
