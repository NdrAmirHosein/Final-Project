class carHistory:
    def __init__(self, CarId, OwnerNationalId, PlateNumber, StartDate, EndDate=None):
        self.carId = CarId
        self.ownerNationalId = OwnerNationalId
        self.startDate = StartDate
        self.endDate = EndDate
        self.plateNumber = PlateNumber
