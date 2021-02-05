import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, clear_mappers

from src.app import app, session
from src.orm import metadata, start_mappers
from src.database import get_session


@pytest.fixture
def client():
    return app.test_client()


@pytest.fixture
def session():
    return get_session('sqlite:///:memory:')
