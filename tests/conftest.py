import pytest
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import os
import subprocess
from sqlalchemy import text
from typing import Generator, Any
from starlette.testclient import TestClient
from main import app
from session import get_db

test_engine = create_engine(
    "postgresql://postgres:postgres@localhost:5433/randomiser_test",
    future=True,
)

test_session = sessionmaker(bind=test_engine, expire_on_commit=False)

CLEAN_TABLES = [
    "test_table"
]


@pytest.fixture(scope="session", autouse=True)
def run_migrations():
    if not os.path.exists("tests/alembic"):
        os.system("alembic init tests/alembic")

    subprocess.run(
        "alembic -c tests/alembic.ini revision --autogenerate -m 'ddd'"
    )
    os.system("alembic -c tests/alembic.ini upgrade heads")


@pytest.fixture(scope="function")
def db():
    engine = create_engine(
        "postgresql://postgres:postgres@localhost:5433/randomiser_test",
        future=True
    )
    _Session = sessionmaker(bind=engine, expire_on_commit=False)
    session = _Session()
    yield session
    session.close()


@pytest.fixture(scope="function", autouse=True)
def clean_tables(db):
    with db as session:
        with session.begin():
            for table in CLEAN_TABLES:
                session.execute(text(f"""TRUNCATE TABLE {table};"""))


@pytest.fixture(scope="function")
def client() -> Generator[TestClient, Any, None]:
    def _get_test_db():
        try:
            with test_session() as session:
                yield session
                session.close()
        finally:
            pass

    app.dependency_overrides[get_db] = _get_test_db
    with TestClient(app=app) as client:
        yield client
