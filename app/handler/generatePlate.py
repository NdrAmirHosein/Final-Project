import random
from app.Database.hashTable_Plate_duality import hashtable
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
    raw_plate = checkX(letter, number)
    check_duality = hashtable()
    if check_incresing_decreasing(raw_plate[0]):
        if check_duality.setData(str(number) + letter, True):
            return True, raw_plate[0]



def finall_plate(cityCode):
    number = randNum()
    letter = setLetter()

    _plate = makePlate(letter, number)
    if _plate[0]:
        finall_plate = plate(str(_plate[1]), cityCode, letter)
        return finall_plate.plate











def check_cityCode(cityCode):
    if cityCode != ("11" or "22" or "31" or "44" or "51" or "61" or "71" or "81" or "91"):
        raise ValueError("Error...!\nCity Code Is Invalide")
    else:
        plate =  finall_plate(cityCode)
        return plate


# 11 | Tehran\n22 | Mashhad\n31 | Isfahan\n44 | Tabriz\n51 | Shiraz\n61 | Ahvaz\n71 | Qom\n81 | Kermanshah\n91 | Urmia