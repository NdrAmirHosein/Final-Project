from app.handler.display_all_registered_cars_and_users import *
from app.data_structures.array import Array

def all_registered_cars():

    return retrive_cars_from_db()

def all_registered_users():
    return retrive_users_from_db()


def all_plates_of_city(city_code):
    city_code = city_code // 10
    return plates_of_city(city_code)

def all_cars_of_city(city_code):
    obj_cars = all_registered_cars()
    
    evaluated_cars = Array()

    for car in obj_cars:
        if int(car.plateNumber.cityCode) == city_code:
            evaluated_cars.append(
                car
            )
    return evaluated_cars 


def search_in_range(startDate, endDate):
    obj_cars = all_registered_cars()

    if startDate and endDate:
        evaluated_cars = Array()
        for car in obj_cars:
            if int(startDate) <= int(car.productionYear) <= int(endDate):
                evaluated_cars.append(
                    car
                )

    elif startDate and endDate == "":
        evaluated_cars = Array()
        for car in obj_cars:
            if int(startDate) == int(car.productionYear):
                evaluated_cars.append(
                    car
                )
    else:
        return obj_cars
    
    return evaluated_cars


def owners_of_city(city_code):
    obj_cars = all_registered_cars()

    evaluated_users = Array()

    for car in obj_cars:
        if int(car.plateNumber.cityCode) == city_code:
            evaluated_users.append(
                car.ownerNationalId
            )

    obj_evaluated_users = Array()
    for nationalId in evaluated_users:
        obj_evaluated_users.append(
            get_one_user(nationalId)
        )
    return obj_evaluated_users


def change_users_name(national_code, new_name):
    user = get_one_user(national_code)
    if user:
        user.name = new_name
        return True
    raise ValueError("UserName Not Found In The Database!!!")


def negative_scores(national_code):
    user = get_one_user(national_code)
    if user.driver:
        return user.penalties
    else:
        raise ProcessLookupError ("You Are Not A Driver!")