from app.data_structures.stack import Stack
from app.data_structures.array import Array


class User:
    def __init__(self, name, lName, birthday, nationalCode, password):

        # if len(nationalCode) != 10:
        #     raise ValueError("\nNational Code Must Be 10 Numbers\n")
        
        self.name = name
        self.l_name = lName
        self.birthday = birthday
        self.national_code = nationalCode
        self.username = nationalCode
        self.password = password


        self.driver = None
        self.owner = None


        self.cars_owned = Array()

class Driver(User):
    def __init__(self, name, l_name, birthday, national_code, licenseId, licenseIssueDate):
        super().__init__(name, l_name, birthday, national_code)
        self.licenseId = licenseId
        self.licenseIssueDate = licenseIssueDate
        self.violationHistory = Stack()