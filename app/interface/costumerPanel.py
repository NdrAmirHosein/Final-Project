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
            if nationalCode[0]:
                print(f"\n  Signup successful! Welcome {nationalCode[1]}\n")
                userPanel(nationalCode[0])


        elif choice == "2":
            
            try:
                national_code = input("Enter Your National Code: ")
                password = input("Enter Your Password: ")
            except ValueError as e:
                print(e)
            check_and_name = login(national_code, password)

            if check_and_name:
                print(f"   Login successful! Welcome {check_and_name}\n")
                userPanel(national_code)
            else:    
                print("\n      Error Log in...!\nUsername Or PassWord IS Wrong!\n")

        elif choice == "3":
            break