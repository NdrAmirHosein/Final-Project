from app.models.users import User
from app.Database.usersDatabase import usersDatabase
def signUp():
    try:
        name = input("\nEnter Your Name: ")
        lName = input("\nEnter Your Last Name: ")
        birthday = input("\nEnter Your Biarthday:(YYYY-MM-DD) ")
        nationalCode = (input("\nPlease Enter Your National Code: "))
        password = input("\nPlease Enter Your Password: ")
        
    except ValueError as e:
        print(e)
    
    