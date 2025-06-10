from app.services.View_registered_vehicles_and_plates import *
from app.services.generateplate import generatePlate

def userPanel(nationalCode):
    while True:
        print("   ...User Panel...  ")
        print("1. Generate Plate")
        print("2. View Registered Vehicles")
        print("3. View Plates Owned")
        print("4. exit")

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
            break