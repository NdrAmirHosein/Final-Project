import json
from app.handler.generatePlate import set_plate_first_time
from app.handler.plate_to_object import _plate
from app.handler.plate_car import set_plate



def read_car_records():
    with open ("app/tests/data/cars_record.json", mode="r", encoding="utf-8") as read_file:
        datas = json.load(read_file)
    for data in datas:
        plate = _plate(data["PlateNumber"], data["OwnerNationalID"])
        set_plate_first_time(plate.cityCode,data["OwnerNationalID"],plate.plate, plate)
    for data in datas:
        set_plate(data["CarID"],data["CarName"],data["Year"],data["PlateNumber"],data["Color"])
    