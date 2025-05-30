from app.Database.usersDatabase import usersDatabase
from app.models.users import User
import bcrypt as bc


def check_nationalCode(national_code):
    if len(national_code) != 10:
        raise ValueError("\nNational Code Must Be 10 Numbers\n")
    return True

def check_len(password):
    if len(password) != 8:
       raise ValueError("\nPassword Must Be 8 Characters\n")
    return True

def isPasswordValid(password):
        isDigit = False
        hasLetter = False

        for char in password:
            if char.isdigit():
                isDigit = True
            elif char.isalpha():
                hasLetter = True
        
        if isDigit:
            if hasLetter:
                return True
            else:
                raise ValueError("\nPassword Must Contains Characters\n")
        else:
            raise ValueError("\nPassword Must Contains Numbers\n")
        

    

def encryption(password):
    if isPasswordValid():
        encrypted_password = bc.hashpw(str(password).encode('utf-8'), bc.gensalt())
        return encrypted_password

def setData(name, lName, birthday, nationalCode, password):
    if check_nationalCode(nationalCode) and check_len(password) and isPasswordValid(password):
        data = User(name, lName, birthday, nationalCode, encryption(password))
        usersDatabase.setUser(nationalCode, data)