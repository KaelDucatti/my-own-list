from app.models import User


def test_create_user():
    user = User(username="alice", email="alice@example.com", password="secret")

    assert user.password == "secret"
