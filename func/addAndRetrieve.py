from func.db import dbgen
import func.aesutil
import pyperclip
from getpass import getpass

from Crypto.Protocol.KDF import PBKDF2
from Crypto.Hash import SHA512
from Crypto.Random import get_random_bytes
import base64

from rich.console import Console
from rich.table import Table

def masterKeys(masterPasswd, saltPhrase):
	passwd = masterPasswd.encode()
	salt = saltPhrase.encode()
	key = PBKDF2(passwd, salt, 32, count=1000000, hmac_hash_module=SHA512)
	return key

def checkEntry(name, url, email, usrname):
	db = dbgen()
	cursor = db.cursor()
	query = f"SELECT * FROM passwdDB.entries WHERE name = '{name}' AND url = '{url}' AND email = '{email}' AND username = '{usrname}'"
	cursor.execute(query)
	results = cursor.fetchall()

	if len(results)!=0:
		return True
	return False

def addEntry(masterPasswd, saltPhrase, name, url, email, usrname):
	if checkEntry(name, url, email, usrname):
		print("-- Entry with these details already exists")
		return
	password = getpass("Enter A Password: ")
	masterKey = masterKeys(masterPasswd, saltPhrase)
	encrypted = func.aesutil.encrypt(key=masterKey, source=password, keyType="bytes")

	#Adding to db
	db = dbgen()
	cursor = db.cursor()
	val = (name, url, email, usrname, encrypted)
	cursor.execute("INSERT INTO passwdDB.entries (name, url, email, username, password) values (%s, %s, %s, %s, %s)", val)
	db.commit()

	print("-- Added Entry into Database")

	db.close()


def getEntry(masterPasswd, saltedPhrase, search, decrypt=False):
	db = dbgen()
	cursor = db.cursor()

	query = ""
	if len(search)==0:
		query = "SELECT * FROM passwdDB.entries"
	else:
		query = "SELECT * FROM passwdDB.entries WHERE"
		for i in search:
			query +=f"{i} ='{search[i]}' AND "
		query = query[:-5]
	cursor.execute(query)
	result = cursor.fetchall()

	if len(result) == 0:
		print("No such Entry found!")
		return

	if(decrypt and len(result)>1) or (not decrypt):
		if decrypt:
			print("Multiple Entries Found")
		displayTable = Table(title="Results")
		displayTable.add_column("Name")
		displayTable.add_column("URL")
		displayTable.add_column("Email")
		displayTable.add_column("Username")

		for i in result:
			displayTable.add_row(i[0], i[1], i[2], i[3])
		console = Console()
		console.print(displayTable)
		return

	if decrypt and len(results)==1:
		masterKey = masterKeys(masterPasswd, saltPhrase)
		decryptedPWD = func.aesutil.decrypt(key=masterKey, source=results[0][4],keyType="bytes")

		print("Password copied to clipboard")
		pyperclip.copy(decryptedPwD.decode())

	db.close()
