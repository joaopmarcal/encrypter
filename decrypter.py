import os
from cryptography.fernet import Fernet

files = []

for file in os.listdir():
    if file == 'encrypter.py' or file == 'thekey.key' or file == 'decrypter.py':
        continue
    if os.path.isfile(file):
        files.append(file)

with open("thekey.key","rb") as key:
    secretKey = key.read()

for file in files:
    with open(file,"rb") as thefile:
        contents = thefile.read()
    contents_decrypted = Fernet(secretKey).decrypt(contents)
    with open(file,"wb") as thefile:
        thefile.write(contents_decrypted)