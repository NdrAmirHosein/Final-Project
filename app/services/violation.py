from app.handler.violation import set_user_and_plate_violation
from app.handler.plate_car import time

def set_violation(license_id, plate, violationLevel, description):

    violationLevel = violationLevel
    violationDate = time()
    set_user_and_plate_violation(license_id, plate, violationDate, violationLevel, description)
    return True
