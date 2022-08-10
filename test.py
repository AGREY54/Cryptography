import base64
import os
from turtle import back
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
password_provided = input("Please type in your password: ")
password_provided = ""
password = password_provided.encode()

salt = b'y\x0f\x9a\xf0\xa2qEy\x1a\x8a\x1c\x9a\xee\x0bU\xba'
kdf = PBKDF2HMAC(algorithm=hashes.SHA256,
                 length=32,
                 salt = salt,
                 iterations=100000,
                 backend=default_backend())

key = base64.urlsafe_b64encode(kdf.derive(password))
file = open('key.key', 'wb')
file.write(key)
print(key)
