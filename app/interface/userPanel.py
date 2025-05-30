from app.services.signUp import signUp

def userPanel():
    while True:
        print("1. SignUp")
        print("2. Exit")

        choice = input("Enter Your Choice: ")
        if choice == "1":
            if signUp():
                print("done")
        elif choice == "2":
            break