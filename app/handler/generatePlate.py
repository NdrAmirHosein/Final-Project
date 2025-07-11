import random
from app.Database.users_database import usersDatabase
from app.Database.plate_database import arrayBST
from app.Database.bloom_filter_plate_duality import BF
from app.data_structures.array import Array
from app.models.plate import plate

def randNum():
    return random.randint(10000, 99999)


def setLetter():
    alphabet = "ABCEFGHIJKLMNOQRSTUVWXYZ"
    letters = Array()
    for char in alphabet:
        letters.append(char)
    
    return letters[randNum() % 23]


def checkX(letter, number):
    odd_numbers = Array()
    for i in range(10):
        if i % 2 == 1:
            odd_numbers.append(i)


    numb = Array()
    for i in str(number):
        numb.append(int(i))
    if letter == "X":
        for i in range(len(numb)):
            if numb[i] % 2 == 0:
                numb[i] = odd_numbers[randNum() % 4]
    finall_number = ""
    for i in range(len(numb)):
        finall_number = finall_number + f"{numb[i]}"
    
    return int(finall_number), letter



def check_incresing_decreasing(number):
    digits = Array()
    for i in str(number):
        digits.append(int(i))
    
    increasing = True
    decreasing = True
    for i in range(len(digits) - 1):
        if digits[i + 1] != digits[i] + 1:
            increasing = False
        if digits[i + 1] != digits[i] - 1:
            decreasing = False
    
    if increasing and decreasing :
        return False
    return True



def makePlate(letter, number):
    _number, _letter = checkX(letter, number)
    check_duality = BF()
    if check_incresing_decreasing(_number):
        if check_duality.check_duality(str(number) + letter):
            return True, _number
        else:
            return False, None



def finall_plate(cityCode):
    while True :
        number = randNum()
        letter = setLetter()

        _flag, _number = makePlate(letter, number)
        if _flag:
            finall_plate = plate(str(_number), cityCode, letter)
            return finall_plate



def array_index_generator(cityCdoe):
    return int(cityCdoe) // 10


def check_cityCode_and_set_Plate(cityCode, nationalCode):

    if cityCode == "11" or cityCode =="22" or cityCode =="31" or cityCode =="44" or cityCode =="51" or cityCode =="61" or cityCode =="71" or cityCode =="81" or cityCode =="91":
        plate =  finall_plate(cityCode)
        index = array_index_generator(cityCode)
        db = usersDatabase()
        user = db.getUser(nationalCode)
        if user.abslout_block != True:
            if user.blockdays == 0:
                plate.owner = nationalCode
                user.plate_owned.append(plate)
                plate_db = arrayBST()
                plate_db.insert_plate(index, plate.plate, plate)
                return plate.plate
            else:
                raise PermissionError(f"User Does Not Have Permission(Penalty Error; Banned For {user.blockdays}  Days)")
        else:
            raise PermissionError("User Is Blocked")
    else:
        raise ValueError("\nError...!\nCity Code Is Invalide\n")



def set_plate_first_time(cityCode, nationalCode, raw_plate, obj_plate):
    index = array_index_generator(cityCode)
    db = usersDatabase()
    user = db.getUser(nationalCode)
    user_plate_history = user.plate_owned
    if obj_plate not in user_plate_history:
        user.plate_owned.append(obj_plate)
    plate_db = arrayBST()
    plate_db.insert_plate(index, raw_plate, obj_plate)
    
