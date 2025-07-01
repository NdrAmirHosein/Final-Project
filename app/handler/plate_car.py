from datetime import datetime
from app.models.car import car
from app.Database.cars_database import cars
from app.models.carHistory import carHistory
from app.models.transaction import transaction
from app.handler.plate_to_object import _plate
# from app.handler.violation import find_plate
from app.models.plateHistory import plateHistory
from app.Database.plate_database import arrayBST
from app.Database.users_database import usersDatabase

def time():
    current_time = datetime.now()
    return current_time.date()

def find_plate_and_activation(plate):
    plate = _plate(plate)
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

def change_palte_atrr_and_history(plate_obj, carId, plate_assignment_date):
    plate_obj.active = True
    plate_obj.vehicleId = carId
    plate_obj.plateHistory.append(
        plateHistory(carId, plate_assignment_date)
    )


def set_plate(carId, carName, year, plate_number, color):
    check_year = check_careDate_and_sys(year)
    plate_obj = find_plate_and_activation(plate_number)
    ownerNationalCode = plate_obj.owner
    if not plate_obj or not check_year:
        return False

    car_db = cars()
    user_db = usersDatabase()
    user_obj = user_db.getUser(ownerNationalCode)
    user_obj.owner = True

    append_car_history(user_obj, carId, ownerNationalCode, plate_obj)
    change_palte_atrr_and_history(plate_obj, carId, check_year)
    insert_car(car_db, carName, year, carId, plate_obj, color, ownerNationalCode)


    return plate_obj.plate ,user_obj.name, user_obj.l_name


def find_plate(plate):

    plate_db = arrayBST()
    return plate_db.get_plate((int(plate.cityCode) // 10), plate.plate)


def transactions_by_carId(carId, newPlateNumber) -> str:
    plate_obj = find_plate_and_activation(newPlateNumber) #NATIONAL CODE DARAD
    
    user_db = usersDatabase()
    car_db = cars()
    car = car_db.find(carId)

    prev_user = user_db.getUser(car.ownerNationalId)
    for history in prev_user.cars_owned:
        if int(history.carId) == int(carId):
            if history.endDate == None:
                history.endDate = time()
    
    preve_plate = car.plateNumber 
    preve_plate.active = False
    for i in range(len(prev_user.cars_owned) -1 ,-1, -1): #not my idea but great one (BACKWARDS)
        if int(prev_user.cars_owned[i].carId) == int(preve_plate.vehicleId):
            prev_user.cars_owned.delete(i)


    preve_plate.vehicleId = None

    user_obj = user_db.getUser(plate_obj.owner)
    car.plateNumber = plate_obj
    car.ownerNationalId = plate_obj.owner

    append_car_history(user_obj, carId, plate_obj.owner, plate_obj)
    change_palte_atrr_and_history(plate_obj, carId, time())

    transaction_obj = transaction(prev_user.national_code, plate_obj.owner, time(), None, preve_plate, plate_obj)
    if len(car.transactionHistory) != 0 :
        car.transactionHistory[len(car.transactionHistory)-1].endDate = time()
    car.transactionHistory.append(
        transaction_obj
    )

    return prev_user.name, prev_user.l_name, user_obj.name, user_obj.l_name, car.name


def transaction_by_plateNumber(plateNumber, newPlateNumber) -> str:
    
    prev_plate = find_plate(_plate(plateNumber)) #OBJECT PREVIOUS PLATE
    plate_obj = find_plate_and_activation(newPlateNumber) #NATIONAL CODE DARAD
    user_db = usersDatabase()
    car_db = cars()

    carId = prev_plate.vehicleId
    car = car_db.find(carId)

    prev_user = user_db.getUser(car.ownerNationalId)
    for history in prev_user.cars_owned:
        if int(history.carId) == int(carId):
            if history.endDate == None:
                history.endDate = time()

    preve_plate = car.plateNumber 
    preve_plate.active = False
    for car_owned in prev_user.cars_owned:
        if car_owned.carId == prev_plate.vehicleId:
            car_owned
    for i in range(len(prev_user.cars_owned) -1 ,-1, -1):
        if int(prev_user.cars_owned[i].carId) == int(prev_plate.vehicleId):
            prev_user.cars_owned.delete(i)
    preve_plate.vehicleId = None


    user_obj = user_db.getUser(plate_obj.owner)
    car.plateNumber = plate_obj
    car.ownerNationalId = plate_obj.owner

    append_car_history(user_obj, carId, plate_obj.owner, plate_obj)
    change_palte_atrr_and_history(plate_obj, carId, time())

    transaction_obj = transaction(prev_user.national_code, plate_obj.owner, time(), None, preve_plate, plate_obj)
    if len(car.transactionHistory) != 0 :
        car.transactionHistory[len(car.transactionHistory)-1].endDate = time()
    car.transactionHistory.append(
        transaction_obj
    )

    return prev_user.name, prev_user.l_name, user_obj.name, user_obj.l_name, car.name