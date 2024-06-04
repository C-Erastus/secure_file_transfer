import crypt 

class secure:
	def __init__(self):
		pass

	def encrypt_password(self, passwd):
		salt = crypt.mksalt(crypt.METHOD_SHA512)
		passwd = crypt.crypt(passwd, salt)

		return paswd

	def verify_user(self, passwd):
		crypt_passwd = self.load_password()
		return crypt.crypt(passwd, crypt_passwd) == crypt_passwd

	def load_password(self):
		with open('app_crendentials', 'r') as file:
			lines = file.readlines()
		return lines[2]

	# encryption and decryption of the credential files

	def encrypt_file(self):
		pass 
	def decrypt_file(self):
		pass 