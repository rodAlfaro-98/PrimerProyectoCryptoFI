from Crypto.Cipher import AES 
from Crypto.Util.Padding import pad, unpad
from read_test import read_keys

data = b'No hay escapatoria, solo queda el duce alivio de la muerte'
keys = read_keys()[0:10]
for key in keys:
    cipher = AES.new(key, AES.MODE_ECB)
    cipher_data = cipher.encrypt(pad(data, AES.block_size))
    original_data = unpad(cipher.decrypt(cipher_data),AES.block_size)
    print(data,cipher_data,original_data)