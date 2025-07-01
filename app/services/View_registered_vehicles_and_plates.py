from app.handler.View_registered_vehicles import car_objs, plate_objs ,find_car_db
from app.data_structures.array import Array
from app.handler.plate_to_object import _plate
from app.handler.violation import find_plate

def show_cars_ownd(nationalCode):
    cars_objs = car_objs(nationalCode)
    return cars_objs

def plate_owned(nationalCode):
    plates_objs = plate_objs(nationalCode)
    return plates_objs

def find_plate_violation(national_code, plate) -> list:
    plate = _plate(plate)
    try:
        founded_plate = find_plate(plate)
    except ValueError as e:
        return False
    if founded_plate.owner == national_code:
        return founded_plate.violationHistory
    else:
        return "This Is Not Your Plate"
    
def retrive_plate_history(plate) -> list:
    plate = _plate(plate)
    cars = Array()
    try:
        founded_plate = find_plate(plate)
        
        for history in founded_plate.plateHistory:
            try:
                car = find_car_db(history.viehcleId)
                cars.append(
                    car
                )
            except ValueError:
                pass
        return cars, founded_plate.plateHistory

    except ValueError as e:
        return False, False
