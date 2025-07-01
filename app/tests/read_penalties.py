import json
from app.handler.violation import set_user_and_plate_violation_first_time
from app.handler.signUp import change_type_date
from app.models.plate import plate

def _plate(rawPlate):
    rawPlate = rawPlate.replace(" ", "")
    plate_part, cityCode = rawPlate.split("-")
    plateNumber = plate_part[:2] + plate_part[3:]
    letter = plate_part[2]
    finall_plate = plate(plateNumber, cityCode, letter,None)
    return finall_plate

def read_peanlty_records():
    with open ("app/tests/data/penalty_records.json", mode="r", encoding="utf-8") as read_file:
        datas = json.load(read_file)
    for data in datas:
        set_user_and_plate_violation_first_time(data["PenaltyID"], data["DriverID"], _plate(data["PlateNumber"]), change_type_date(data["PenaltyDate"]),data["PenaltyLevel"], data["Description"])
