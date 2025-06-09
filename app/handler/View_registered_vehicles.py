from app.Database.users_database import usersDatabase
from app.Database.cars_database import cars
from app.data_structures.array import Array

def cars_owned(nationalId):
    users_db = usersDatabase()

    user = users_db.getUser(nationalId)

    cars_owned = user.cars_owned
    cars = Array()
    for car in cars_owned:
        cars.append(
            car.carId
        )
    return cars

def find_car_db(carId):
    cars_db = cars()
    return cars_db.find(str(carId))


def car_objs(nationalId):
    cars = cars_owned(nationalId)
    
    car_objs = Array()
    for car in cars:
        car_obj = find_car_db(int(car))
        if car_obj not in car_objs:
            car_objs.append(
                car_obj
            )
    
    return car_objs
