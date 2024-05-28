
class registraton:

    @property
    def name(self):
        return self._name
    @property
    def email(self):
        return self._email

    @name.setter
    def name(self, name):
        self._name = name

    @email.setter
    def email(self, email):
        self._email = email)

