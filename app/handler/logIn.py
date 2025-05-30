from bcrypt import checkpw
from app.handler.signUp import check_nationalCode, check_len, isPasswordValid
from app.Database.usersDatabase import usersDatabase

def logIn(national_code, password):
    try:
        if check_nationalCode(national_code) and check_len(password) and isPasswordValid(password):
            db = usersDatabase()
            data = db.getUser(national_code)
            if checkpw(str(password).encode('utf-8'), data.password):
                print(f"   Login successful! Welcome {data.name}\n")
                return True
    except:
        return False