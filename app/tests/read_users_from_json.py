import json
from app.handler.signUp import setData


def read_user_data():
    with open("app/tests/users_records.json", mode="r", encoding="utf-8") as write_file:
        datas = json.load(write_file)
    
    for data in datas:
        setData(data["FirstName"],data["LastName"], data["DateOfBirth"], data["NationalID"], data["Password"])
