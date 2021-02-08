import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import clear_mappers

from src.adapters.orm import metadata
from src.entrypoints.app import app
from src.database import get_session
from src.domain import model


@pytest.fixture
def client():
    return app.test_client()


@pytest.fixture
def session():
    return get_session('sqlite:///:memory:')
