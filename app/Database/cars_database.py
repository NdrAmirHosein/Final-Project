from app.data_structures.bst import BinarySearchTree

class cars:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(cars, cls).__new__(cls, *args, **kwargs)
        return cls._instance
    
    def __init__(self):
        if not hasattr(self, 'initialized'):
            self.initialized = True
            self.cars = BinarySearchTree()

    def set_cars(self, carId:int, obj_car):
        self.cars.insert(carId, obj_car)
    
    def find(self, carId):
        return self.cars.search(carId).value.value
    
    def delete(self, carId) -> bool:
        return self.cars.delete(carId)
