import json 
from app.services.retrive_cars_plates_users_information import get_one_user
from app.data_structures.array import Array
from app.Phase4.sorting import radix_sort
from app.Phase4.userModels import phase4

def convert_timeObj_to_int(obj_time) -> int:
    dt_object = obj_time
    formatted_string = dt_object.strftime("%Y%m%d")

    integer_representation = int(formatted_string)

    return integer_representation


def get_driver_license_date() -> list:
    with open ("app/tests/data/phase4.json", mode="r", encoding="utf-8") as read_file:
        datas = json.load(read_file)
    
    license_dates = Array()
    for data in datas:
        user = get_one_user(data["NationalID"])
        license_dates.append(
            phase4(user.national_code,convert_timeObj_to_int(user.license_issue_date),data["NegativePoints"],user.license_issue_date)
        )

    sorted_arr = radix_sort(license_dates)

    return sorted_arr
