#!/usr/bin/python3

import hashlib
import Crypto
import hmac
from Crypto.Cipher import AES
import time
import socket

key = b'strawhatpirateee' # Byte format key
iv = b'piratekingstraww' # Byte format initialization vector

def pad(s): # For adding extra spaces so the message is supplied as 16-byte blocks
    block_size = 16
    remainder = len(s) % block_size
    padding_needed = block_size - remainder
    return s + padding_needed * ' '


node = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port_and_ip = ('127.0.0.1', 4444)
node.bind(port_and_ip)   
node.listen(1) 
cnn, addr = node.accept() 

print ("Connection from: " + str(addr) )

msg = input("Message: ")
AES = AES.new(key, AES.MODE_CBC, iv)
pad = pad(msg)
encrypted = AES.encrypt(pad) # Encrypting the padded message.
msg_unicode = msg.encode('utf-8')
hsh_hmac = hmac.new(key,msg_unicode,hashlib.sha512)
cnn.send(encrypted)
#time.sleep(2)
cnn.send(hsh_hmac.hexdigest().encode('utf-8'))

node.close()
