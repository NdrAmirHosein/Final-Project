from app.models.plate import plate
def _plat(rawPlate):
    # plate_input = "34G653-61"
    rawPlate = rawPlate.replace(" ", "")
    plate_part, cityCode = rawPlate.split("-")  # "34G653", "61"
    plateNumber = plate_part[:2] + plate_part[3:]  # "34" + "653" = "34653"
    letter = plate_part[2]  # "G"
    finall_plate = plate(plateNumber, cityCode, letter)
    return finall_plate