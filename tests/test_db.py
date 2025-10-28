from app.models import User


def test_create_user(session):
    user = User(username="alice", email="alice@example.com", password="secret")

    session.add(user)
    session.commit()

    assert user.password == "secret"
