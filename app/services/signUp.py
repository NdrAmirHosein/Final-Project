from app.handler.signUp import setData
def signUp():
    try:
        name = input("\nEnter Your Name: ")
        lName = input("\nEnter Your Last Name: ")
        birthday = input("\nEnter Your Biarthday:(YYYY-MM-DD) ")
        nationalCode = (input("\nPlease Enter Your National Code: "))
        password = input("\nPlease Enter Your Password: ")
        seted_data = setData(name, lName, birthday, nationalCode, password)
        if seted_data:
            return nationalCode, seted_data
        else:
            return None
    except ValueError as e:
        print(e)
