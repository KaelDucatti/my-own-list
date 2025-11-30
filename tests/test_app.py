from http import HTTPStatus

from fastapi.testclient import TestClient

from my_own_list.app import app


def test_read_root_returns_hello_fastapi():
    client = TestClient(app)

    response = client.get('/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Hello, FastAPI'}
