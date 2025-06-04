from app.data_structures.array import Array
class car:
    def __init__(self, name, productionYear, vehicleId, plateNumber, color, ownerNationalId):
        self.name = name
        self.productionYear = productionYear
        self.vehicleId = vehicleId
        self.plateNumber = plateNumber
        self.color = color
        self.ownerNationalId = ownerNationalId

        self.startDate = None
        self.endDate = None


        self.transactionDate = Array()
        