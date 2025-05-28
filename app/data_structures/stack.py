class Stack:
    def __init__(self, size=100):
        self.stack = [None] * size
        self.size = size
        self.pointer = 0

    def push(self, data):
        if self.pointer == self.size:
            raise OverflowError
        self.stack[self.pointer] = data
        self.pointer += 1
        return True
    
    def pop(self):
        if self.pointer == 0:
            raise IndexError
        self.stack[self.pointer -1] = None
        self.pointer -= 1
        return True
    
    def size(self):
        return self.pointer + 1
        
    def __str__(self):
        return str(self.stack)
