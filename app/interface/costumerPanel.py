from app.services.signUp import signUp
from app.interface.usersPanel import userPanel
from app.services.logIn import login

def costumerPanel():
    while True:
        print("1. Sign Up")
        print("2. Log In")
        print("3. Exit")

        choice = input("Enter Your Choice: ")
        if choice == "1":
            nationalCode = signUp()
            if nationalCode:
                userPanel(nationalCode)
        elif choice == "2":
            nationalCode = login()
            if nationalCode:
                userPanel(nationalCode)
        elif choice == "3":
            break