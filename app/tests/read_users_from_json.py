import json
from app.handler.signUp import setData


def read_user_data():
    with open("app/tests/data/users_records.json", mode="r", encoding="utf-8") as read_file:
        datas = json.load(read_file)

    for data in datas:
        setData(data["FirstName"],data["LastName"], data["DateOfBirth"], data["NationalID"], data["Password"])
