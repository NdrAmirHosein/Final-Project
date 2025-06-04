from app.services.plate_car import plate_car

def adminlogin():
    while True:
        print("1. Log In")
        print("2. Exit")

        choice = input("Enter Your Choice: ")
        if choice == "1":
            username = input("Enter Your Username: ")
            password = input("Enter Your Password: ")
            adminPage(username, password)

        elif choice == "2":
            break

def adminPage(username, password):

    if username == "admin" and password == "admin":
        pass
    else:
        raise ValueError("ridi admin jan")
    
    while True:
        print("1. Plate A Car")
        print("2. Exit")

        choice = input("Enter Your Choice: ")

        if choice == "1":
            plate_car()
        elif choice == "2":
            break
