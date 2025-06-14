from app.data_structures.hashTable import HashTable
from app.data_structures.bloom_filter import BloomFilter

class BF:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(BF, cls).__new__(cls, *args, **kwargs)
        return cls._instance
    
    def __init__(self):
        if not hasattr(self, 'initialized'):
            self.initialized = True
            self.bf = BloomFilter()
    
    def check_duality(self, key):
        if self.bf.lookup(key):
            return False 
        else:
            self.bf.add(key)
            return True


