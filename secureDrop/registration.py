
class _registration:
    def __init__(self):
        self.name = None
        self.email = None 
        self.passwd = None 

    def get_name(self):
        self.name = input("Enter Full Name: ")

    def get_email(self):
        self.email = input("Enter Email Address: ")

    def get_password(self):
        passwd = input("Enter Password: ")
        _passwd = input("Re-enter Password: ")

        while (passwd != _passwd):
            print("Passwords didn't match")
            passwd = input("Enter Password: ")
            _passwd = input("Re-enter Password: ")
        self.passwd = passwd
        print("\nPasswords Match\nExiting SecureDrop")

    """@property
    def name(self):
        return self._name
    @property
    def email(self):
        return self._email

    @name.setter
    def name(self, name):
        self.name = name

    @email.setter
    def _email(self, email):
        self._email = email

    def test_func(self):
        print("Testing_regristration calls")"""

