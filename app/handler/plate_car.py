from datetime import datetime
from app.models.car import car
from app.models.carHistory import carHistory
from app.Database.cars_database import cars
from app.Database.plate_database import arrayBST
from app.Database.users_database import usersDatabase
from app.handler.plate_to_object import _plat

def time():
    current_time = datetime.now()
    return current_time.date()

def find_plate_and_activation(plate):
    plate = _plat(plate)
    plate_db = arrayBST()
    obj_plate = plate_db.get_plate((int(plate.cityCode) // 10), plate.plate)

    if obj_plate.plate == plate.plate and obj_plate.active == False:
        return obj_plate # plak moojod boode va gheyr faal asst. mitavand sabt shavad
    else:
        raise ValueError("\nPlate Is Not Valid\n")

def change_type_carYear(carYear):
    return datetime.strptime(carYear, "%Y").date().year

def check_careDate_and_sys(carYear):
    carYear = change_type_carYear(carYear)
    sysTime = time()
    if carYear > sysTime.year:
        raise ValueError("\nCar Year Can Not Be After Today...\n")
    else:
        return sysTime # tarikh plack va system ok ast mitavan plak sabt kard
    

def append_car_history(user_obj, car_Id, owner_id, plate_obj):
    for history in user_obj.cars_owned:
        if int(history.carId) == int(car_Id):
            if history.endDate:
                user_obj.cars_owned.append(
                    carHistory(car_Id, owner_id, plate_obj, history.endDate)
                )
            else:
                user_obj.cars_owned.append(
                    carHistory(car_Id, owner_id, plate_obj, time())
            )
                
    user_obj.cars_owned.append(
            carHistory(car_Id, owner_id, plate_obj, time())
    )

def insert_car(car_db, carName, year, carId, plate_obj, color, ownedID):
    car_db.set_cars(
        carId,
        car(carName, year, carId, plate_obj, color, ownedID)
    )

def change_palte_atrr_and_history(plate_obj, carId, year):
    plate_obj.active = True
    plate_obj.vehicleId = carId
    plate_obj.plateHistory.append(
        (carId, year)
        #check shavad khahashan ba 
    )


def set_plate(carId, carName, year, plate_number, color, ownerNationalId):
    check_year = check_careDate_and_sys(year)
    plate_obj = find_plate_and_activation(plate_number)
    if not plate_obj or not check_year:
        return False

    car_db = cars()
    user_db = usersDatabase()
    user_obj = user_db.getUser(ownerNationalId)
    user_obj.owner = True

    append_car_history(user_obj, carId, ownerNationalId, plate_obj)
    change_palte_atrr_and_history(plate_obj, carId, check_year)
    insert_car(car_db, carName, year, carId, plate_obj, color, ownerNationalId)

    return plate_obj.plate ,user_obj.name, user_obj.l_name