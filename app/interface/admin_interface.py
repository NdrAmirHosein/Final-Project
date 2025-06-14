from app.services.retrive_cars_plates_users_information import *
from app.services.driving_license import *
from app.services.plate_car import *
from app.services.signUp import signUp

def adminlogin():
    while True:
        print("1. Log In")
        print("2. Exit")

        choice = input("Enter Your Choice: ")
        if choice == "1":
            try:
                username = input("Enter Your Username: ")
                password = input("Enter Your Password: ")
                adminPage(username, password)
            except Exception as e:
                print(e)
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
        print("6. Search Cars In Rnage Of Production Year")
        print("7. Display All Owners Of A City")
        print("8  Set New Name For User")
        print("9. Granting A Driving License")
        print("10 Delete User License")
        print("11 Display All Drivers")
        print("12. Exit")

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
            try:
                startDate = input("Enter Your Start Date(YYYY): ")
                endDate = input("Enter Your End Date(YYYY): ")
            except ValueError as e:
                print(e)
            obj_cars = search_in_range(startDate, endDate)
            for car in obj_cars:
                print(car.name, "---", car.productionYear, "---", car.color, "---", car.plateNumber.plate)

        elif choice == "7":
            try:
                print("11 | Tehran\n22 | Mashhad\n31 | Isfahan\n44 | Tabriz\n51 | Shiraz\n61 | Ahvaz\n71 | Qom\n81 | Kermanshah\n91 | Urmia")
                city_code = int(input("Enter City Code: "))
            except ValueError as e:
                print(e)
            
            obj_users = owners_of_city(city_code)
            for user in obj_users:
                print(user.name, "---", user.l_name, "---", user.national_code)

        elif choice == "8":
            try:
                national_code = input("Enter User National Code: ")
                new_user_name = input("Enter New Name: ")
                if change_users_name(national_code, new_user_name):
                    print("New user Name set")
            except ValueError as e:
                print(e)

        elif choice == "9":
            try:
                national_code = input("Enter User National Code: ")
                licenseID, name = Issuance_driving_license(national_code)
                if not licenseID:
                    print("User Not Found")
                    national_code, name = signUp()
                    licenseID, name = Issuance_driving_license(national_code)
                    print(f"LicenseID {licenseID} For New User {name} Has Been Created.")
                else:
                    print(f"LicenseID {licenseID} For User {name} Has Been Created.")
            except Exception as e:
                print(e)
                
        elif choice == "10":
            try:
                national_code = input("Enter User National Code: ")
                check = delete_driving_license(national_code)
                if check:
                    print("User License Deleted Succesfully.")
            except Exception as e:
                print(e)
        
        elif choice == "11":
            drivers = show_all_drivers()
            print("Driver License  ---  National Code  ---  License Issue Date")
            for driver in drivers:
                print(driver.licenseId, "---", driver.national_code, "---", driver.license_issue_date)
        
        elif choice == "12":
            break
