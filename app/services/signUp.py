from app.handler.signUp import setData
def signUp():
    try:
        name = input("\nEnter Name: ")
        lName = input("\nEnter Last Name: ")
        birthday = input("\nEnter Biarthday:(YYYY-MM-DD) ")
        nationalCode = (input("\nPlease Enter National Code: "))
        password = input("\nPlease Enter Password: ")
        seted_data = setData(name, lName, birthday, nationalCode, password)
        if seted_data:
            return nationalCode, seted_data
        else:
            raise ValueError("Incorrect inputs")
    except ValueError as e:
        print(e)
