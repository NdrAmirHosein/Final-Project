from app.Database.users_database import usersDatabase
from app.models.carHistory import carHistory
from app.Database.cars_database import cars
from app.handler.plate_to_object import _plate

def setOwnership(nationalCode, carId, PlateNumber, startDate, endDate):
    db = usersDatabase()

    user = db.getUser(nationalCode)
    plate = _plate(PlateNumber, nationalCode)
    _car_history = carHistory(carId, nationalCode, plate, startDate, endDate)
    user.cars_owned.append(_car_history)
