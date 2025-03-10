from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column
from base import Base


class TestModelnumber(Base):
    __tablename__ = "test_table"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    number: Mapped[int] = mapped_column(Integer)


class TestModelString(Base):
    __tablename__ = "test_string"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    msg: Mapped[str] = mapped_column(String)


