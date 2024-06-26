from registration import _registration
from login import login

def help():
	
	print("add	-> Add a new contact")
	print("list	->	List all online contacts")
	print("send	->	Transfer file to contact")	

if __name__ == "__main__":

	reg = _registration()
    _login = login()

	command = input()
	# check the data base to see if the user is register
	print("\n")
	if command == "secureDrop":
		ret = input("Do you want to register a new user (y/n)?: ")
		if ret == "y":
			reg.get_name()
			reg.get_email()
			reg.get_password()
        elif ret == "n":
            _login.get_email()
            _login.get_password()
            
            command = input("Type "help" for Commands")
            
