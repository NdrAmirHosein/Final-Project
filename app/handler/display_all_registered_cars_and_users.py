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
    if user:
        return user
    else:
        return False


def plates_of_city(city_code):

    plates_db = arrayBST()
    plates_of_city = plates_db.retrive_information(city_code)

    return plates_of_city