from bitarray import bitarray
import math
import mmh3

class BloomFilter:
    def __init__(self, expected_nums=1000000, salt=None):
        self.size = self.size_of_bitarray(expected_nums)
        self.num_hashes = self.number_of_hash_functions(expected_nums)
        self.salt = salt or '' # this is for reducing collisions and prevents reverse engeneering
        self.bit_array = bitarray(self.size)
        self.bit_array.setall(0)
    def add(self, element):
        """
        Add a new bits of data to the bit array
        """

        for i in range(self.num_hashes):
            digset = mmh3.hash((str(self.salt) + str(element) + str(i)).encode('utf-8'))
            index = abs(digset) % self.size
            self.bit_array[index] = 1

    def lookup(self, element):
        """
        search for an element in the set. To check that absoultly negetive
        or maybe already available
        """
        for i in range(self.num_hashes):
            digset = mmh3.hash((str(self.salt) + str(element) + str(i)).encode('utf-8'))
            index = abs(digset) % self.size
            if self.bit_array[index] == 0:
                return False
        return True
    
    def size_of_bitarray(self, expected_nums):
        # accuracy of 0.001 %
        # 3MB of storage
        m = -(expected_nums * math.log(0.00001)) / (math.log(2)) ** 2
        return int(m)
    
    # m stands for size of bit array
    # n stands for expected elements to be inserted
    def number_of_hash_functions(self, expected_nums):
        k = ((self.size_of_bitarray(expected_nums)) / expected_nums) * math.log(2)
        return int(k)
    