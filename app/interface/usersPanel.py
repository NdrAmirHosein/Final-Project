from app.services.View_registered_vehicles import show_cars_ownd
from app.services.generateplate import generatePlate

def userPanel(nationalCode):
    while True:
        print("   ...User Panel...  ")
        print("1. Generate Plate")
        print("2. View Registered Vehicles")
        print("3. exit")

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
            for car in cars:
                print(car.vehicleId, car.name)

        elif choice == "3":
            break