from sqlalchemy import create_engine

from src.orm import metadata


def get_engine(db):
    engine = create_engine(db)
    metadata.create_all(engine)
    return engine


def get_test_uri():
    return 'sqlite:///:memory:'


def get_postgres_uri():
    host = os.environ.get('DB_HOST', 'localhost')
    port = 54321 if host == 'localhost' else 5432
    password = os.environ.get('DB_PASSWORD', 'abc123')
    user, db_name = 'accounting', 'accounting'
    return f"postgresql://{user}:{password}@{host}:{port}/{db_name}"
