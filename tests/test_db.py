from dataclasses import asdict

from sqlalchemy import select

from app.models import User


def test_create_user(session):
    new_user = User(
        username="alice", email="alice@example.com", password="secret"
    )

    session.add(new_user)
    session.commit()

    user = session.scalar(select(User).where(User.username == "alice"))

    assert asdict(user) == {
        "id": 1,
        "username": "alice",
        "email": "alice@example.com",
        "password": "secret",
    }
