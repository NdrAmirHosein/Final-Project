from app.Database.drivers_database import DrriverDatabase
from app.Database.users_database import usersDatabase
from app.Database.plate_database import arrayBST
from app.Database.cars_database import cars

def retrive_cars_from_db():
    cars_db = cars()
    return cars_db.cars._preorder()


def retrive_users_from_db():
    users = usersDatabase().usersDatabase
    return users.values

def get_one_user(national_code):
    users_db = usersDatabase()
    user = users_db.getUser(national_code)
    return user if user else False


def plates_of_city(city_code):

    plates_db = arrayBST()
    plates_of_city = plates_db.retrive_information(city_code)

    return plates_of_city

def get_one_driver(licenseID):
    drivers_db = DrriverDatabase()
    driver = drivers_db.getUser(licenseID)
    return driver if driver else False

def delete_car_fromDB(carId) -> str:
    cars_db = cars()
    founded_car = cars_db.find(carId)
    plate = founded_car.plateNumber
    plate.active = False
    plate.vehicleId = None
    cars_db.delete(carId)
    return plate.plate
    

def transaction_historyDB(carId) -> object:
    car_db = cars()
    founded_car = car_db.find(carId)
    return founded_car if founded_car else False