from model import TestModelnumber


def test_get():
    ...


# @router.patch("/")
# def update_number(old_number: int, new_number: int, db: Session = Depends(get_db)) -> dict:
#     number_for_update = db.query(TestModelnumber).filter(TestModelnumber.number == old_number).first()
#     if number_for_update is None:
#         return {"status_code": 404, "message": f"Number {old_number} not defiend"}
#
#     number_for_update.number = new_number
#     db.add(number_for_update)
#     db.commit()
#     db.flush()
#     return {"status_code": 200, "message": "OK"}
def test_update(db, client):
    n = TestModelnumber(number=100)
    db.add(n)
    db.commit()
    db.flush()

    response = client.patch(f"/", params={"old_number": 100, "new_number": 101})
    assert response.json()["status_code"] == 200
    assert response.json()["message"] == "OK"

    number_for_update = db.query(TestModelnumber).filter(TestModelnumber.number == 101).first()

    assert number_for_update is not None
    assert number_for_update.number == 100


def test_post(db, client):
    #запрос на роут
    response = client.post(f"/", params={"number": 100})
    #проверка что ответ пришел правильно
    assert response.json()["status_code"] == 200
    assert response.json()["message"] == "OK"
    # сделаем запрос в бд на проверку зап
    number = db.query(TestModelnumber).filter(TestModelnumber.number == 100).first()

    #преврим что записалось правильно
    assert number is not None
    assert number.number == 100


def test_delete():
    ...
