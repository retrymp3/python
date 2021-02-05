#!/usr/bin/python3

import hmac
import hashlib
from Crypto.Cipher import AES
import Crypto
import socket


key = "strawhatpirateee"

# remove the extra spaces at the end
def unpad(s):
	return s.rstrip()

# Needs the same salt and iv as the encryption function.
# Needs the same configurations for scypt and aes functions as in the encryption function.
def decrypt(salt,aes_text,iv,key):
	private_key = hashlib.scrypt(key.encode(), salt=salt, n=2**14, r=8, p=1, dklen=32)
	aes = AES.new(private_key, AES.MODE_CBC, iv)
	decrypted_msg = aes.decrypt(aes_text)
	unpaded_msg = unpad(decrypted_msg)
	return unpaded_msg
	
def hash_hmac(hsh_hmac,msg_byte_decode):
	hsh_hmac_decode = hsh_hmac.decode()
	msg_byte_encode = msg_byte_decode.encode()
	return (hsh_hmac_decode,msg_byte_encode)
    
node = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port_and_ip = ('127.0.0.1', int(input("Port: ")))
node.connect(port_and_ip)

iv = node.recv(1024)
salt = node.recv(1024)
aes_text = node.recv(1024)
hsh_hmac =  node.recv(1024)

decrypted = decrypt(salt,aes_text,iv,key)
msg_byte_decode = decrypted.decode()

hsh_hmac_decode,msg_byte_encode = hash_hmac(hsh_hmac,msg_byte_decode)
new_hsh_hmac = hmac.new(key.encode(),msg_byte_encode,hashlib.sha512)
new_hsh_hmac_hex = new_hsh_hmac.hexdigest()

while aes_text:
	if  (hsh_hmac_decode == new_hsh_hmac_hex):
		print('Server: ' + msg_byte_decode) 
		aes_text = node.recv(1024)
	else:
		print("The message has been tampered with, please exit the session")
		break
node.close() 
