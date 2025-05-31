from app.data_structures.hashTable import HashTable
class hashtable:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(hashtable, cls).__new__(cls, *args, **kwargs)
        return cls._instance
    
    def __init__(self):
        if not hasattr(self, 'initialized'):
            self.initialized = True
            self.ht = HashTable()
    
    def setData(self, key, data):

        if self.ht[key] != False:
            return False
        if self.ht[key] is False:
            self.ht[key] = data
            return True