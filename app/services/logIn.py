from app.handler.logIn import logIn
def login():
    try:
        national_code = input("Enter Your National Code: ")
        password = input("Enter Your Password: ")
        check = logIn(national_code, password)
    except ValueError as e:
        print(e)


    if check:
        return True
    else:
        print("\n      Error Log in...!\nUsername Or PassWord IS Wrong!\n")