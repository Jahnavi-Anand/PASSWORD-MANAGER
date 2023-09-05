import random
import string
from getpass import getpass

from Crypto.Protocol.KDF import PBKDF2
from Crypto.Hash import SHA512
from Crypto.Random import get_random_bytes
import base64


def generatePassword(length):
	return ''.join([random.choice(string.ascii_letters + string.digits + string.punctuation) for n in range(length)])
