def get_max(objects):
    max_int = objects[0].license_date_int
    for object in objects:
        if object.license_date_int > max_int:
            max_int = object.license_date_int
    return max_int


def counting_sort(arr, digit_place):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    for num in arr:
        digit = (num.license_date_int // digit_place) % 10
        count[digit] += 1
    
    for i in range(1, 10):
        count[i] += count[i - 1]
    
    for i in range(n-1, -1 ,-1):
        digit = (arr[i].license_date_int // digit_place) % 10
        count[digit] -= 1
        output[count[digit]] = arr[i]
    return output

def radix_sort(arr):

    max_num = get_max(arr)
    
    digit_place = 1
    while max_num // digit_place > 0:
        arr = counting_sort(arr, digit_place)
        digit_place *= 10
    
    return arr


# This Sorting Is customized for sort objects base of one of there attribiutes
