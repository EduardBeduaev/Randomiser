from fastapi import APIRouter, Depends
from model import TestModelnumber, TestModelString
from sqlalchemy.orm import Session
from session import get_db
from random import randint
from typing import List

router = APIRouter()


@router.get("/")
def get_numbers(db: Session = Depends(get_db)) -> List[int]:
    numbers = db.query(TestModelnumber).all()
    return [x.number for x in numbers]


@router.get("//")
def get_string(db: Session = Depends(get_db)) -> List[str]:
    strings = db.query(TestModelString).all()
    return [x.msg for x in strings]


@router.post("/")
def post_number(number: int, db: Session = Depends(get_db)) -> dict:
    try:
        test_n = TestModelnumber(number=number)
        db.add(test_n)
        db.commit()
        db.flush()
    except Exception:
        return {"status_code": 400, "message": "Error"}

    return {"status_code": 200, "message": "OK"}


@router.post("//")
def post_string(msg: str, db: Session = Depends(get_db)) -> dict:
    try:
        test_str = TestModelString(msg=msg)
        db.add(test_str)
        db.commit()
        db.flush()
    except Exception:
        return {"status_code": 400, "message": "Error"}

    return {"starus_code": 200, "message": "OK"}


@router.delete("/")
def delete_(number: int, db: Session = Depends(get_db)) -> dict:
    number_for_delete = db.query(TestModelnumber).filter(
        TestModelnumber.number == number).first()  #ORM Object Relation Mapping
    if number_for_delete is None:
        return {"status_code": 404, "message": f"Number {number} not defiend"}
    db.delete(number_for_delete)
    db.commit()
    db.flush()
    return {"status_code": 200, "message": f"OK"}


@router.delete("//")
def delete_srting_(msg: str, db: Session = Depends(get_db)) -> dict:
    string_for_delete = db.query(TestModelString).filter(TestModelString.msg == msg).first()
    if string_for_delete is None:
        return {"status_code": 404, "message": f"String {msg} not defiend"}

    db.delete(string_for_delete)
    db.commit()
    db.flush()
    return {"status_code": 200, "message": "OK"}


@router.patch("/")
def update_number(old_number: int, new_number: int, db: Session = Depends(get_db)) -> dict:
    number_for_update = db.query(TestModelnumber).filter(TestModelnumber.number == old_number).first()
    if number_for_update is None:
        return {"status_code": 404, "message": f"Number {old_number} not defiend"}

    number_for_update.number = new_number
    db.add(number_for_update)
    db.commit()
    db.flush()
    return {"status_code": 200, "message": "OK"}


@router.patch("//")
def update_string(old_string: str, new_string: str, db: Session = Depends(get_db)) -> dict:
    string_for_update = db.query(TestModelString).filter(TestModelString.msg == old_string).first()
    if string_for_update is None:
        return {"status_code": 404, "message": f"String {old_string} not defiend"}

    string_for_update.msg = new_string
    db.add(string_for_update)
    db.commit()
    db.flush()
    return {"status_code": 200, "message": "OK"}
