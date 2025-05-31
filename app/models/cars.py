from data_structures.array import Array
from app.models.plate import plate
class car:
    def __init__(self, name, productionYear, vehicleId, plateNumber, color):
        self.name = name
        self.productionYear = productionYear
        self.vehicleId = vehicleId
        self.plateNumber = plate() # need to check i mean this will need handler
        self.color = color


        self.transactionDate = Array()
        