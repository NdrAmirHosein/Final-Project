from app.handler.signUp import setData
def signUp():
    try:
        name = input("\nEnter Your Name: ")
        lName = input("\nEnter Your Last Name: ")
        birthday = input("\nEnter Your Biarthday:(YYYY-MM-DD) ")
        nationalCode = (input("\nPlease Enter Your National Code: "))
        password = input("\nPlease Enter Your Password: ")
        setData(name, lName, birthday, nationalCode, password)
    except ValueError as e:
        print(e)
    
    return True