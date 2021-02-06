import pytest

from src.entrypoints.app import app
from src.database import get_session


@pytest.fixture
def client():
    return app.test_client()


@pytest.fixture
def session():
    return get_session('sqlite:///:memory:')
