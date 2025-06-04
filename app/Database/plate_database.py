from app.data_structures.array import Array
from app.data_structures.bst import BinarySearchTree
class arrayBST:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(arrayBST, cls).__new__(cls, *args, **kwargs)
        return cls._instance
    
    def __init__(self):
        if not hasattr(self, 'initialized'):
            self.initialized = True
            self.array = Array()
            self.bst = BinarySearchTree()

    def insert_plate(self, cityCode, plate, obj_plate):
        if len(self.array) == 0:
            for _ in range(11):
                self.array.append(None)

        if self.array[cityCode] is None:
            self.array[cityCode] = BinarySearchTree()
        self.array[cityCode].insert(plate, obj_plate)

    def get_plate(self, city_code, plate):
        return self.array[city_code].search(plate).value.value
    