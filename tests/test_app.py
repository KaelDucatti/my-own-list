from http import HTTPStatus


def test_root_return_ok_and_message(client):
    response = client.get("/")  # act

    assert response.status_code == HTTPStatus.OK  # assert
    assert response.json() == {"message": "Hello, FastAPI!"}  # assert


def test_hello_return_ok_and_html(client):
    response = client.get("/hello")

    assert response.status_code == HTTPStatus.OK
    assert "<h1>Hello</h1>" in response.text


def test_create_user(client):
    response = client.post(
        "/users/",
        json={
            "username": "alice",
            "email": "alice@example.com",
            "password": "secret",
        },
    )

    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        "id": 1,
        "username": "alice",
        "email": "alice@example.com",
    }
