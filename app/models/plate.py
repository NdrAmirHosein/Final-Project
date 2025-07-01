from app.data_structures.array import Array

class plate:
    def __init__(self, plateNumber, cityCode, letter, owner_nCode=None):
        self.plateNumber = plateNumber
        self.cityCode = cityCode
        self.letter = letter
        self.plate = f"{self.plateNumber[:2]} {self.letter} {self.plateNumber[2:]} - {self.cityCode}"

        self.owner = owner_nCode
        
        self.active = False
        self.vehicleId = None


        self.plateHistory = Array()

        self.violationHistory = Array()

