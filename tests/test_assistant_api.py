import pytest
from api.assistant_api import app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_dummy():
    assert True


# def test_home_get(client):
#     response = client.get('/')
#     assert response.status_code == 200
#     assert response.get_json() == {'data': 'hello world'}


# def test_home_post(client):
#     response = client.post('/')
#     assert response.status_code == 405  # Method Not Allowed
