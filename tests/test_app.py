from http import HTTPStatus

from fastapi.testclient import TestClient

from app.app import app


def test_root_return_ok_and_message():
    client = TestClient(app)  # arrange

    response = client.get("/")  # act

    assert response.status_code == HTTPStatus.OK  # assert
    assert response.json() == {"message": "Hello, FastAPI!"}  # assert


def test_hello_return_ok_and_html():
    client = TestClient(app)

    response = client.get("/hello")

    assert response.status_code == HTTPStatus.OK
    assert "<h1>Hello</h1>" in response.text
