from app.services.retrive_cars_plates_users_information import *
from app.services.plate_car import *

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
        print("2. Display All Registerd Cars")
        print("3. Display All Users")
        print("4. Diaplay All Plates Of A City")
        print("5. Display All Cars Of A City")
        print("6. Exit")

        choice = input("Enter Your Choice: ")

        if choice == "1":
            try:
                carId = check_carId()
                carName = input("Enter Vehicle Name: ")
                year = input("Enter The Date Of Manufacture Of Vehicle: ")
                plate_number = input("Enter License Plate Number: ")
                print("Enter Vehicle Color: ")
                print("WT : White\nBC : Black\nRD : Red\nBL : Blue\nGR : Silver or Gray\nOT : Other")
                color = input()
                color = check_input_color(color)
                ownerNationalID = input("Enter The Owner Nationial ID: ")
            except ValueError as e:
                print(e)

            datas = plate_car(carId, carName, year, plate_number, color, ownerNationalID)
            if datas:
                print(f"Plate ({datas[0]}) Dedicated To Car {carName} For User: {datas[1]} {datas[2]}")

        elif choice == "2":
            obj_cars = all_registered_cars()
            print("Car Name  ---  ID  ---  Plate  ---  Year")
            for car in obj_cars:
                print(car.name,"---",car.vehicleId, "---", car.plateNumber.plate, "---",car.productionYear)  
        
        elif choice == "3":
            obj_users = all_registered_users()
            print("First Name  ---  Last Name  ---  National Code\n")
            for user in obj_users:
                print(user.name,"  ---  ", user.l_name, "  ---  ", user.national_code)
        
        elif choice == "4":
            try:
                
                print("11 | Tehran\n22 | Mashhad\n31 | Isfahan\n44 | Tabriz\n51 | Shiraz\n61 | Ahvaz\n71 | Qom\n81 | Kermanshah\n91 | Urmia")
                city_code = int(input("Enter City Code: "))
            except ValueError as e:
                print(e)

            obj_plates = all_plates_of_city(city_code)
            print("Plates  ---  Status")
            for plate in obj_plates:
                print(plate.plate, plate.active)
        
        elif choice == "5":
            try:
                print("11 | Tehran\n22 | Mashhad\n31 | Isfahan\n44 | Tabriz\n51 | Shiraz\n61 | Ahvaz\n71 | Qom\n81 | Kermanshah\n91 | Urmia")
                city_code = int(input("Enter City Code: "))
            except ValueError as e:
                print(e)

            obj_cars = all_cars_of_city(city_code)
            print("Plate --- Name --- ID --- Color --- Owner Natinoal ID")
            for car in obj_cars:
                print(car.plateNumber.plate, "---", car.name, "---", car.vehicleId, "---", car.color, "---", car.ownerNationalId)

        elif choice == "6":
            break
