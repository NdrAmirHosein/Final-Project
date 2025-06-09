from app.handler.plate_car import set_plate

def plate_car(carId, carName, year, plate_number, color, ownerNationalID):

    return set_plate(carId, carName, year, plate_number, color, ownerNationalID)
    


def check_input_color(color):

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