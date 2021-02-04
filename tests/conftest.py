import pytest
from sqlalchemy.orm import clear_mappers, sessionmaker

from src.app import app


@pytest.fixture
def client():
    return app.test_client()
