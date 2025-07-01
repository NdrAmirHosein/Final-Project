from app.handler.plate_car import transactions_by_carId, transaction_by_plateNumber

def transaction_car(carId_or_PlateNumber, newPlateNumber):
    if len(carId_or_PlateNumber) == 5:
        return transactions_by_carId(carId_or_PlateNumber, newPlateNumber)
    elif len(carId_or_PlateNumber.replace(" ", "")) == 9:
        return transaction_by_plateNumber(carId_or_PlateNumber, newPlateNumber)
    