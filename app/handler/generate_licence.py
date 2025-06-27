from app.Database.bloom_filter_LicenceID_duality import BF
from app.Database.users_database import usersDatabase
from app.Database.drivers_database import DrriverDatabase
from app.handler.plate_car import time
import random

check_duality = BF()
drivers_db = DrriverDatabase()

def rand_numb():
    return random.randint(10000000, 99999999)

def create_licenceID():
    while True:
        licenseID = rand_numb()
        if check_duality.check_duality(licenseID):
            return licenseID

def calculate_age(birthday):
    today = time()
    age = today.year - birthday.year - ((today.month, today.day) < (birthday.month, birthday.day)) # man naboodam
    return age

def set_licenceID_for_user(national_code):
    user_db = usersDatabase()
    
    user = user_db.getUser(national_code)
    if calculate_age(user.birthday) >= 18:
        licenseID = create_licenceID()

        user.driver = True
        user.licenseId = licenseID
        user.license_issue_date = time()

        drivers_db.setUser(str(licenseID), national_code)

        return licenseID, user.name
    else:
        raise PermissionError("User Is Under 18...")


def set_licenseID_first_time(national_code, driverID, licenseDate):
    user_db = usersDatabase()
    user = user_db.getUser(national_code)

    if calculate_age(user.birthday) >= 18:
        user.driver = True
        user.licenseId = driverID
        user.license_issue_date = licenseDate

        drivers_db.setUser(driverID, national_code)