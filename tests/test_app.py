from http import HTTPStatus


def test_read_root_returns_hello_fastapi(client):
    response = client.get("/")

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {"message": "Hello, FastAPI"}


def test_created_user_returns_user_public_schema(client):
    response = client.post(
        "/users/",
        json={
            "username": "Kael",
            "email": "kael@gmail.com",
            "password": "ocruel",
        },
    )

    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        "username": "Kael",
        "email": "kael@gmail.com",
    }
