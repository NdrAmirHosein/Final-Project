from app.Database.bloom_filter_violationId import BF
from app.models.violation import violation
from app.Database.drivers_database import DrriverDatabase
from app.Database.users_database import usersDatabase
from app.Database.plate_database import arrayBST
from app.services.driving_license import delete_driving_license
from app.handler.plate_to_object import _plate
from app.handler.signUp import change_type_date

import random

def rand_numb():
    violationID = random.randint(100000, 999999)
    return violationID

def generate_violationId():
    check_duality = BF()
    while True:
        violationId = rand_numb()
        if check_duality.check_duality(violationId):
            return violationId

def identify_penalty(violationLevel):
    if violationLevel == "Low":
        return 1, 10
    elif violationLevel == "Medium":
        return 3, 30
    elif violationLevel == "High":
        return 5, 50



def nationalCode_from_driverId(licenseId):
    driver_db = DrriverDatabase()
    driver_national_code = driver_db.getUser(licenseId)
    return driver_national_code


def set_violation_obj(licenseId, plate, violationDate, violationLevel, description):
    violation_id = generate_violationId()
    penalty_days, penalty_points = identify_penalty(violationLevel)
    # violationDate = change_type_date(violationDate) shayad badan estefade shod
    plate = _plate(plate, nationalCode_from_driverId(licenseId))
    violation_obj = violation(violation_id, licenseId, plate, violationDate, violationLevel, penalty_days, penalty_points, description)

    return violation_obj

def find_plate(plate):

    plate_db = arrayBST()
    return plate_db.get_plate((int(plate.cityCode) // 10), plate.plate)

def set_user_and_plate_violation(licenseId, plate, violationDate, violationLevel, description):

    user_db = usersDatabase()
    driver_national_code = nationalCode_from_driverId(licenseId)

    violation_obj = set_violation_obj(licenseId, plate, violationDate, violationLevel, description)


    founded_plate = find_plate(violation_obj.plate)
    founded_plate.violationHistory.append(
        violation_obj
    )

    user = user_db.getUser(driver_national_code)
    user.violation_History.append(
        violation_obj
    )

    user.penalties += violation_obj.penaltyPoints
    if user.penalties >= 500:
        delete_driving_license(user.national_code)
        print("fucked up shodi")
        user.abslout_block = True
    user.blockdays += violation_obj.penalty_days


def set_user_and_plate_violation_first_time(violationid, licenseId, plate, violationDate, violationLevel, description):

    user_db = usersDatabase()
    driver_national_code = nationalCode_from_driverId(licenseId)

    penalty_days, penalty_points = identify_penalty(violationLevel)
    violation_obj = violation(violationid, licenseId, plate, violationDate, violationLevel, penalty_days, penalty_points, description)


    founded_plate = find_plate(violation_obj.plate)
    founded_plate.violationHistory.append(
        violation_obj
    )

    user = user_db.getUser(driver_national_code)
    user.violation_History.append(
        violation_obj
    )

    user.penalties += violation_obj.penaltyPoints
    if user.penalties >= 500:
        delete_driving_license(user.national_code)
        print("fucked up shodi")
        user.abslout_block = True
    user.blockdays += violation_obj.penalty_days