from app.services.retrive_cars_plates_users_information import get_one_user
from app.handler.generate_licence import set_licenceID_for_user
from app.services.retrive_cars_plates_users_information import all_registered_users
from app.data_structures.array import Array


def Issuance_driving_license(national_code):
    user = get_one_user(national_code)
    if user:
        if not user.driver:
            return set_licenceID_for_user(national_code)
        else:
            raise ValueError (f"You Are A driver And Your Licence ID is {user.licenseId}")
    else:
        return False, False
    
def delete_driving_license(national_code):
    user = get_one_user(national_code)

    if user:
        user.driver = False
        user.licenseId = None
        user.license_issue_date = None
        user.penalties = 0
        user.blockdays = 0
        return True
    else:
        raise ValueError("User Not Found!!!")


def show_all_drivers():
    users = all_registered_users()

    drivers = Array()
    for user in users:
        if user.driver:
            drivers.append(
                user
            )
    return drivers