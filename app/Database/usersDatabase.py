from app.data_structures.hashTable import HashTable
class usersDatabase:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(usersDatabase, cls).__new__(cls, *args, **kwargs)
        return cls._instance
    
    def __init__(self):
        if not hasattr(self, 'initialized'):
            self.userDatabase = HashTable()
            
    def setUser(self, nationalCode, data):
        self.userDatabase[nationalCode] = data
        print(f"\n  Signup successful! Welcome {data.name}\n")
    
