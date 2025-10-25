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


def test_list_users(client):
    response = client.get("/users/")

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        "users": [
            {
                "id": 1,
                "username": "alice",
                "email": "alice@example.com",
            }
        ]
    }


def test_update_user(client):
    response = client.put(
        "/users/1/",
        json={
            "username": "alice",
            "email": "alice@example.com",
            "password": "secret",
        },
    )

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        "username": "alice",
        "email": "alice@example.com",
        "id": 1,
    }


def test_update_user_404(client):
    response = client.put(
        "/users/2/",
        json={
            "username": "alice",
            "email": "alice@exemple.com",
            "password": "secret",
        },
    )

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {"detail": "User not found"}


def test_detail_user(client):
    response = client.get("/users/1/")

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        "username": "alice",
        "email": "alice@example.com",
        "id": 1,
    }


def test_delete_user(client):
    response = client.delete("/users/1/")

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        "username": "alice",
        "email": "alice@example.com",
        "id": 1,
    }


def test_delete_user_404(client):
    response = client.delete("/users/2/")

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {"detail": "User not found"}
