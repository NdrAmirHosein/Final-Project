from app.interface.main_interface import interface
from app.tests.read_users_from_json import read_user_data
from app.tests.read_ownership_cars import read_ownership_car
from app.tests.read_car_records import read_car_records
from app.tests.read_drivers_record import read_drivers_records
from app.tests.read_penalties import read_peanlty_records


read_user_data()
read_ownership_car()
read_car_records()
read_drivers_records()
read_peanlty_records()
interface()