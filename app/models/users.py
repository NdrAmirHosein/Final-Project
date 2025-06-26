from app.data_structures.array import Array


class User:
    def __init__(self, name, lName, birthday, nationalCode, password):

        self.name = name
        self.l_name = lName
        self.birthday = birthday
        self.national_code = nationalCode
        self.username = nationalCode
        self.password = password


        self.driver = False
        self.owner = False

        self.cars_owned = Array()
        self.plate_owned = Array()

        self.licenseId = None
        self.license_issue_date = None
        self.penalties = 0
        self.blockdays = 0

        self.abslout_block = False

        self.violation_History = Array()


# class Driver:
#     def __init__(self, User:User, licenseId, license_issue_date, penalties, blockdays):
#         self.user = User
#         self.licenseId = licenseId
#         self.license_issue_date = license_issue_date
#         self.penalties = 0
#         self.blockdays = 0

#         self.violation_History = Array()