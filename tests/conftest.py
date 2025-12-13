import pytest
from fastapi.testclient import TestClient

from my_own_list.app import app


@pytest.fixture
def client():
    return TestClient(app)
