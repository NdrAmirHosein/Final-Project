from app.handler.View_registered_vehicles import car_objs, plate_objs

def show_cars_ownd(nationalCode):
    cars_objs = car_objs(nationalCode)
    return cars_objs

def plate_owned(nationalCode):
    plates_objs = plate_objs(nationalCode)
    return plates_objs