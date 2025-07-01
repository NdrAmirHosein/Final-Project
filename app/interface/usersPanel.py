from app.services.View_registered_vehicles_and_plates import *
from app.services.retrive_cars_plates_users_information import negative_scores,view_violation_history
from app.services.generateplate import generatePlate

def userPanel(nationalCode):
    while True:
        print("   ...User Panel...  ")
        print("1. Generate Plate")
        print("2. View Registered Vehicles")
        print("3. View Plates Owned")
        print("4. View Negative Scores")
        print("5. View Violation History")
        print("6. View Violation Of One Plate")
        print("7. View Plate History")
        print("8. Exit")

        choice = input("Enter Your Choice: ")

        if choice == "1":
            try:
                print("11 | Tehran\n22 | Mashhad\n31 | Isfahan\n44 | Tabriz\n51 | Shiraz\n61 | Ahvaz\n71 | Qom\n81 | Kermanshah\n91 | Urmia")
                cityCode = input("Enter Your City Code: ")
            except ValueError as e :
                print(e)

            plate = generatePlate(nationalCode, cityCode)
            print(f"\nPlate generated successfully: {plate}\n")
        
        elif choice == "2":
            cars = show_cars_ownd(nationalCode)
            print("CarId --- Car Name --- Color --- Car Plate")
            for car in cars:
                print(car.vehicleId,"---", car.name,"---", car.color,"---", car.plateNumber.plate)

        elif choice == "3":
            print("Plates Owned:\nPlates    ----      Status")
            plates = plate_owned(nationalCode)
            for plate in plates:
                print(plate.plate, " ---> ", plate.active)
        
        elif choice == "4":
            try:
                neg_scores = negative_scores(nationalCode)
                print(f"Negative Scores: {neg_scores}")
            except Exception as e:
                print(e)
        
        elif choice == "5":
            try:
                violation_history = view_violation_history(nationalCode)

                print("Date Of Violation  ---  Plate Of Violation  --- Violation Level  --- Descreaption")
                for violation in violation_history:
                    print(violation.violationDate , " --- " , violation.plate.plate , " --- " , violation.violationLevel , " --- " , violation.description)
            except LookupError as e:
                print(e)
            except AttributeError as ae:
                print(ae)

        elif choice == "6":
            try:
                print("Plates Owned:\nPlates    ----      Status")
                plates = plate_owned(nationalCode)
                for plate in plates:
                    print(plate.plate, " ---> ", plate.active)
                if len(plates) != 0 :
                    plate = input("Enter Your Plate: ")
                    plate_violation_history = find_plate_violation(nationalCode, plate)
                    if plate_violation_history != False:
                        if len(plate_violation_history) == 0:
                            print("There Is No Violation History For This Plate")

                        elif type(plate_violation_history) == str:
                            print(plate_violation_history)

                        else:
                            for violation in plate_violation_history:
                                print(violation.violationDate , " --- " , violation.plate.plate , " --- " , violation.violationLevel , " --- " , violation.description)
                    else:
                        print("Not Such Plate Available")
                else:
                    print("You Dont Have Plate")

            except ValueError as e:\
            print(e)
        
        elif choice == "7":
            try:
                print("Plates Owned:\nPlates    ----      Status")
                plates = plate_owned(nationalCode)
                for plate in plates:
                    print(plate.plate, " ---> ", plate.active)
                if len(plates) != 0 :
                    plate = input("Enter Your Plate: ")
                    car_information, plate_history = retrive_plate_history(plate)
                    if car_information and plate_history:
                        print("\nCar and Plate History:")
                        for i in range(len(car_information)):
                            print(f"Car: {car_information[i].name}, Year: {car_information[i].productionYear}, Color: {car_information[i].color}")
                            print(f"Assigned on: {plate_history[i].plate_assignment_date}\n")
                    else:
                        print("Not Such A Car Found")
                else:
                    print("You Dont Have Plate")
                
            except:
                pass

        elif choice == "8":
            break