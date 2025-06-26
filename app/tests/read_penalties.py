import json
from app.handler.violation import set_user_and_plate_violation_first_time
from app.handler.signUp import change_type_date
from app.handler.plate_to_object import _plat

def read_peanlty_records():
    with open ("app/tests/data/penalty_records.json", mode="r", encoding="utf-8") as read_file:
        datas = json.load(read_file)
    for data in datas:
        set_user_and_plate_violation_first_time(data["PenaltyID"], data["DriverID"], _plat(data["PlateNumber"]), change_type_date(data["PenaltyDate"]),data["PenaltyLevel"], data["Description"])
