from data_structures.array import Array

class plate:
    def __init__(self, plateNumber, cityCode, letter):
        self.plateNumber = plateNumber
        self.cityCode = cityCode
        self.letter = letter

        
        self.active = False
        self.vehicleId = None


        self.plateHistory = Array()

        self.violationHistory = None

