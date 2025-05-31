from app.Database.usersDatabase import usersDatabase
from app.handler.plate_to_object import _plat
def setOwnership(nationalCode, carId, startDate, EndDtae, PlateNumber):
    db = usersDatabase()

    user = db.getUser(nationalCode)
    plate = _plat(PlateNumber)
    user.cars_owned.append((carId, startDate, EndDtae, plate))

    print(user.cars_owned)