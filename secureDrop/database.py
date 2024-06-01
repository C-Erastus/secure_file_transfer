import mysql.connector 

config = {
	'user': 'root',
	'password': '',
	'host': '127.0.0.1',
	'raise_on_warnings': True
}

cnx = mysql.connector.connect(**config)
cnx.close()