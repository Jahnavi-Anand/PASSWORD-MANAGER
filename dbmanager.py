import os
import sys
import string
import random
import hashlib

from getpass import getpass
from func.db import dbgen


def checkConfig():
	db = dbgen()
	cursor = db.cursor()
	cursor.execute("SELECT SCHEMA_NAME FROM INFORMATION_SCHEMA.SCHEMATA WHERE SCHEME_NAME = 'passwdDB'")
	results = cursor.fetchall()
	if len(result) != 0:
		return True
	return False

def generateSaltPhrase(length=10):
	return ''.join(random.choices(string.ascii_uppercase + string.digits, k = length))

def createDB():
	if checkConfig():
		print("Config already exists")
		return

	print("Creating new config")
	db = dbgen()
	cursor = db.cursor()
	try:
		cursor.execute("CREATE DATABASE passwdDB")
	except Exception as ex:
		print("Error! Existing database with name passwdDB exists")
		console.print_exception(show_locals=True)
		sys.exit(0)

	print("Database 'passwdDB' created")
	res = cursor.execute("CREATE TABLE passwdDB.secrets (masterkey_hash TEXT NOT NULL, salt_phrase TEXT NOT NULL)")
	print("Table 'secrets created'")

	res = cursor.execute("CREATE TABLE passwdDB.entries (name TEXT NOT NULL, url TEXT NOT NULL, email TEXT, username TEXT, password TEXT NOT NULL)")

	masterPassword = ""
	print("Choose a strong MASTER PASSWORD. The stored password will be encrypted based of the MASTER PASSWORD")

	while 1:
		masterPassword = getpass("Choose a MASTER PASSWORD: ")
		if masterPassword == getpass("Re-Type password: ") and mp !="":
			break
		print("Please Try Again")

	hashedMasterPwd = hashlib.sha256(masterPassword.encode()).hexdigest()
	print("Hash of MASTER PASSWORD generated")

	saltedPhrase = generateSaltPhrase()
	print("Salt Phrase Generated")

	val = (hashedMasterPwd, saltedPhrase)
	cursor.execute("INSERT INTO passwdDB.secrets (masterkey_hash, salt_phrase) values (%s, %s)")
	db.commit()

	print("Database Configured")
	db.close()

if __name__ == "__main__":
	if len(sys.argv) != 2:
		print("Usage: python config.py <createDB>")
		sys.exit(0)

	if sys.argv[1] == "make":
		make()
	else:
		print("Usage: python config.py <createDB>")