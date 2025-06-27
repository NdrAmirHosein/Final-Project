from app.data_structures.hashTable import HashTable
class DrriverDatabase:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(DrriverDatabase, cls).__new__(cls, *args, **kwargs)
        return cls._instance
    
    def __init__(self):
        if not hasattr(self, 'initialized'):
            self.initialized = True
            self.drivers_db = HashTable()
            
    def setUser(self, licenseID, national_code):
        self.drivers_db[licenseID] = national_code
        return True
    
    def getUser(self, licenseID):
        return self.drivers_db[licenseID]