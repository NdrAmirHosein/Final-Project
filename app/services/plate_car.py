from app.handler.plate_car import set_plate

def plate_car():
    try:
        carId = check_carId()
        carName = input("Enter Vehicle Name: ")
        year = input("Enter The Date Of Manufacture Of Vehicle: ")
        plate_number = input("Enter License Plate Number: ")
        color = check_input_color()
        OwnerNationalID = input("Enter The Owner Nationial ID: ")
    except ValueError as e:
        print(e)


    message = set_plate(carId, carName, year, plate_number, color, OwnerNationalID)
    if message:
        print(message)

def check_input_color():
    try:
        print("Enter Vehicle Color: ")
        print("WT : White\nBC : Black\nRD : Red\nBL : Blue\nGR : Silver or Gray\nOT : Other")
        color = input()
    except ValueError as e:
        print(e)

    if color == "WT" or color =="BC" or color =="RD" or color =="BL" or color =="GR" or color =="OT":
        return color
    else:
        raise ValueError("Color Is Not Valid")
    
def check_carId():
    try:
        carId = input("Enter VehicleId: ")
    except ValueError as e:
        print(e)
    
    if len(carId) != 5 :
        raise ValueError("Car ID Must Be 5 Numbers")
    
    return carId