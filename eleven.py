import os
from cryptography.fernet import Fernet

files = []
for file in os.listdir():
    if file == "vecna.py" or file == "thekey.key" or file == "eleven.py":
        continue
    if os.path.isfile(file):
        files.append(file)

with open("thekey.key","rb") as key:
    skey = key.read()

for file in files:
    with open(file,"rb") as thefile:
        contents = thefile.read()
    decrypt = Fernet(skey).decrypt(contents)
    with open(file,"wb") as thefile:
        thefile.write(decrypt)
