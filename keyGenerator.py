import os
from Crypto.Random import get_random_bytes
keys = []

for i in range(666):
    keys.append(str(get_random_bytes(32)))
keyFile = open("Keys.txt","w")
for key in keys:
    keyFile.write(key[2:32])
    keyFile.write('\n')
keyFile.close()