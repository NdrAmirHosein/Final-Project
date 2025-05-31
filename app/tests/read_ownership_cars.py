import json
from app.handler.set_ownership_cars import setOwnership


def read_ownership_car():
    with open ("app/tests/data/ownership_history.json", mode="r", encoding="utf-8") as read_file:
        datas = json.load(read_file)
    for data in datas:
        setOwnership(data["OwnerNationalID"], data["CarID"], data["StartDate"], data["EndDate"], data["PlateNumber"])

    