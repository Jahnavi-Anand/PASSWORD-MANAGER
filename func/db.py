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
