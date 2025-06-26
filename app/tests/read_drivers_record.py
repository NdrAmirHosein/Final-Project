import json
from app.handler.generate_licence import set_licenseID_first_time
from app.handler.signUp import change_type_date

def read_drivers_records():
    with open ("app/tests/data/drivers_record.json", mode="r", encoding="utf-8") as read_file:
        datas = json.load(read_file)
    for data in datas:
        set_licenseID_first_time(data["NationalID"], data["DriverID"], change_type_date(data["LicenseDate"]))
