from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from src.adapters.orm import metadata


def get_session(db_uri):
    engine = create_engine(db_uri)
    metadata.create_all(bind=engine)
    return scoped_session(sessionmaker(autocommit=False,
                                       autoflush=False,
                                       bind=engine))
