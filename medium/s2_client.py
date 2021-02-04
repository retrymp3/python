#!/usr/bin/python3

import hmac
import hashlib
from Crypto.Cipher import AES
import Crypto
import socket


key = b'strawhatpirateee'
iv = b'piratekingstraww'

def unpad(s): # remove the extra spaces at the end
    return s.rstrip()
 
    
node = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port_and_ip = ('127.0.0.1', 4444) 
node.connect(port_and_ip)

AES = AES.new(key, AES.MODE_CBC, iv)

enc_msg = node.recv(1024)
hsh_hmac =  node.recv(1024)
# enc_msg_decode = enc_msg.decode()
hsh_hmac_decode = hsh_hmac.decode()
decrypt_msg = AES.decrypt(enc_msg)
unpaded_msg = unpad(decrypt_msg)
msg_byte_decode = unpaded_msg.decode('utf-8')
unpaded_msg_unicode = msg_byte_decode.encode('utf-8')

new_hsh_hmac = hmac.new(key,unpaded_msg_unicode,hashlib.sha512)
new_hsh_hmac_hex = new_hsh_hmac.hexdigest()
while enc_msg:
	if  (hsh_hmac_decode == new_hsh_hmac_hex):
		print('Server: ' + msg_byte_decode) 
		enc_msg = node.recv(1024) 
	 
node.close() 

