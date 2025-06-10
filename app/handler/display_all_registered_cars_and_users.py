from app.Database.users_database import usersDatabase
from app.Database.cars_database import cars

def retrive_cars_from_db():
    cars_db = cars()
    return cars_db.cars._preorder()


def retrive_users_from_db():
    users = usersDatabase().usersDatabase
    return users.values