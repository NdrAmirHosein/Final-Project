import ctypes 
# Provides C-compatible data types and ways to interact with C-style memory,
# “ctype” is library that allows us to access low level C implementations in python



class Array(object):

    def __init__(self):
        self.item_count = 0
        self.array_capacity = 1
        self.primary_array = self._create_array(self.array_capacity)


    def _create_array(self, array_capacity):
        return (array_capacity * ctypes.py_object)() # a special type that represents a generic Python object in the C-style memory.
    


    def __len__(self):
        return self.item_count
    


    def __getitem__(self, item_index):
        """
        return element at index k
        """

        if not 0 <= item_index < self.item_count:
            raise IndexError("index out of range!")
        return self.primary_array[item_index]
    

    
    def __setitem__(self, item_index, value):
        """
        Assign a value to the array at a specific index
        """
        if not 0 <= item_index < self.array_capacity:
            raise IndexError("index out of range!")
        self.primary_array[item_index] = value
    


    def append(self, item):
        """
        Add new item to array, increse capacity if not available
        """

        if self.item_count == self.array_capacity:
            self._enlarge_array(2 * self.array_capacity)
        self.primary_array[self.item_count] = item
        self.item_count += 1



    def _enlarge_array(self, new_capacity):
        """
        create array with input capacity and copy the contents of old to new array
        """

        secondary_array = self._create_array(new_capacity)
        for i in range(self.item_count):
            secondary_array[i] = self.primary_array[i]

        self.primary_array = secondary_array
        self.array_capacity = new_capacity



    def delete(self, item_index):
        if 0 > item_index or item_index > self.item_count -1 :
            raise IndexError("index out of range!")
        
        while 0 <= item_index < self.item_count -1 :
            self.primary_array[item_index] = self.primary_array[item_index + 1] # nice techniqe
            item_index += 1
        self.item_count -= 1
    
    def __iter__(self):
        for i in range(self.item_count):
            yield self.primary_array[i]

    def __repr__(self):
        """
        String representation for debugging.
        """
        return "[" + ", ".join(repr(self.primary_array[i]) for i in range(self.item_count)) + "]"
