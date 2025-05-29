import bcrypt as bc

class Password:
    def __init__(self, password):
        if len(password) != 8:
            raise ValueError("\nPassword Must Be 8 Characters\n")
        self.password = password
    
    
    def isPasswordValid(self):
        isDigit = False
        hasLetter = False

        for char in self.password:
            if char.isdigit():
                isDigit = True
            elif char.isalpha():
                hasLetter = True
        
        if isDigit:
            if hasLetter:
                return True
            else:
                raise ValueError("\nPassword Must Contains Characters\n")
        else:
            raise ValueError("\nPassword Must Contains Numbers\n")
        

    

    def encryption(self):
        if self.isPasswordValid():
            encrypted_password = bc.hashpw(str(self.password).encode('utf-8'), bc.gensalt())
            return encrypted_password
    