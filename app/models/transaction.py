class transaction:
    def __init__(self, prev_owner, now_owner, startDate, endDate, prev_plate, now_plate):
        self.prev_owner = prev_owner
        self.now_owner = now_owner
        self.start_date = startDate
        self.endDate = endDate
        self.prev_plate = prev_plate
        self.now_plate = now_plate
