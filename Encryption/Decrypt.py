import sys

import cryptography
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.fernet import Fernet

import base64

raw = input("String: ") # input of the encrypted string

password_provided = input("Password: ")  # input of password
password = password_provided.encode()  # Convert to type bytes

salt = b'\xb5\x0fug\xb9\x06\x8e\xfa\xebJ\xc1\xfe\xd9\x9e\x9e\xfe'
kdf = PBKDF2HMAC(
    algorithm=hashes.SHA256,
    length=32,
    salt=salt,
    iterations=100000,
    backend=default_backend()
)
key = base64.urlsafe_b64encode(kdf.derive(password))  # Can only use kdf once

from cryptography.fernet import Fernet
encrypted = raw.encode()

try:
    f = Fernet(key)
    decrypted = f.decrypt(encrypted)  # Decrypt the bytes. The returning object is of type bytes

    print(f'\n{decrypted.decode()}')
except cryptography.fernet.InvalidToken:
    print("\nInvalid password")

input('Press ENTER to exit') 