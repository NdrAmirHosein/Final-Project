from app.handler.View_registered_vehicles import car_objs

def show_cars_ownd(nationalCode):
    cars_objs = car_objs(nationalCode)
    return cars_objs