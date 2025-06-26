from bcrypt import checkpw
from app.handler.signUp import check_nationalCode, check_len, isPasswordValid
from app.Database.users_database import usersDatabase

def logIn(national_code, password):
    try:
        if check_nationalCode(national_code) and check_len(password) and isPasswordValid(password):
            db = usersDatabase()
            user = db.getUser(national_code)
            # if checkpw(str(password).encode('utf-8'), data.password):
            if user.password == password:
                if user.abslout_block == False:
                    return user.name
                else:
                    raise PermissionError("User Is Abslout Blocked")
    except:
        return False