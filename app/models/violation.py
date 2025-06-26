class violation:
    def __init__(self, violationId, licenceId, plate, violationDate, violationLevel,penalty_days, penaltyPoints, description):
        self.violationId = violationId
        self.violationLevel = violationLevel
        self.penalty_days = penalty_days
        self.penaltyPoints = penaltyPoints

        self.licenceId = licenceId
        self.plate = plate
        self.violationDate = violationDate
        self.description = description
        
    