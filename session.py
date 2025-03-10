from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from typing import Generator

engine = create_engine("postgresql://postgres:postgres@localhost:5432/randomiser")
_session = sessionmaker(bind=engine, expire_on_commit=False, class_=Session)


def get_db() -> Generator:
    try:
        session: Session = _session()
        yield session
    finally:
        session.close()


