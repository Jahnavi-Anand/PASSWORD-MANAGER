<<<<<<< HEAD
import mysql.connector

def dbgen():
	try:
		db = mysql.connector.connect(
			host ="localhost",
			user ="passwdDB",
			passwd ="qwerty"
		)
	except Exception as ex:
		print("Error occured! Unable to connect to database")

	return db
=======
import mysql.connector

def dbgen():
	try:
		db = mysql.connector.connect(
			host ="localhost",
			user ="passwdDB",
			passwd ="qwerty"
		)
	except Exception as ex:
		print("Error occured! Unable to connect to database")

return db
>>>>>>> 3ccfe46e8f9938ae96700fa9b1023ca0618db014
