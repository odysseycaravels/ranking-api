from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from ranking_api.config import get_config
from ranking_api.model import Base


def get_connection_str():
    return get_config()['conn_str']


def get_engine():
    return create_engine(get_connection_str())


def get_session():
    return sessionmaker(bind=get_engine())()


def create_tables():
    Base.metadata.create_all(get_engine())


def drop_tables():
    Base.metadata.drop_all(get_engine())


def renew_tables():
    drop_tables()
    create_tables()
