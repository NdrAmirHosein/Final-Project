from data_structures.array import Array
class car:
    def __init__(self, name, productionYear, vehicleId, plateNumber, color):
        self.name = name
        self.productionYear = productionYear
        self.vehicleId = vehicleId
        self.plateNumber = plateNumber
        self.color = color


        self.transactionDate = Array()
        