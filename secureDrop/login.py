import getpass
from registration import _registration
from security import secure

class login:

    def __init__(self):
        self._email = None
        self._password = None
        self._reg = _registration()
        self._secure = secure()

    def get_email(self):
        self._reg.get_email() 
    
    def get_password(self):    
        self._password = getpass.getpass("Enter Password: ")   

    def verify_user(self):
        if  self._secure.verify_user(self._password):
            print("Welcome to SecureDrop")
            
        
