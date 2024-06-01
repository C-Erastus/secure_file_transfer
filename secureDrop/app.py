from registration import _registration


if __name__ == "__main__":

	reg = _registration()

	command = input()
	# check the data base to see if the user is register
	print("\n")
	if command == "secureDrop":
		ret = input("Do you want to register a new user (y/n)?: ")
		if ret == "y":
			reg.get_name()
			reg.get_email()
			reg.get_password()
		
