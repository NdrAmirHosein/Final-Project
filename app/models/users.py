from data_structures.stack import Stack



class User:
    def __init__(self, name, lName, birthday, nationalCode):
        self.name = name
        self.l_name = lName
        self.birthday = birthday
        self.national_code = nationalCode
        self.username = nationalCode
        self.password = None


        self.driver = None
        self.owner = None

class Driver(User):
    def __init__(self, name, l_name, birthday, national_code, licenseId, licenseIssueDate):
        super().__init__(name, l_name, birthday, national_code)
        self.licenseId = licenseId
        self.licenseIssueDate = licenseIssueDate
        self.violationHistory = Stack()