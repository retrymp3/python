#!/usr/bin/python3

import hashlib
import Crypto
import hmac
from Crypto.Cipher import AES
import time
import socket
import os
from Crypto import Random

key = "strawhatpirateee"

# For adding extra spaces at the endso the message becomes a multiple of 16 in bytes.
# AES needs 16 byte blocks
def pad(s):
    block_size = 16
    remainder = len(s) % block_size
    padding_needed = block_size - remainder
    return s + padding_needed * ' '

# Creating a private key by adding the salt to the key.
# IV is used so that it can prevent duplicate characters in the cipher text.
# Salt is generated randomly each time the script is run.
# Scrypt is used for making a more secure private key.
# N - Cost factor, r - Block size, p - parallelization factor
def encrypt(msg, key):
	salt = os.urandom(AES.block_size) # Generating a random salt.
	iv = Random.new().read(AES.block_size) # Generating a random initialization vector.
	private_key = hashlib.scrypt(key.encode(), salt=salt, n=2**14, r=8, p=1, dklen=32) # Creating a private key by adding salt.
	aes = AES.new(private_key, AES.MODE_CBC, iv) # Configuring the encryption mode to CBC(Cipher Blocker Chaining)
	padded_text = pad(msg)
	aes_text = aes.encrypt(padded_text)
	return (aes_text,salt,iv)

# AF_INET specifies the ipv4 address family.
# SOCK_STREAM specifies the TCP socket.
node = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port_and_ip = ('127.0.0.1', int(input("Port: ")))
node.bind(port_and_ip)   # Assigns an ip and port number to the socket instance.
node.listen(1) # Limits the number of connections
cnn, addr = node.accept() # Listens for an incomming connection and upon connection it returns a (host,port) tuple.

print ("Connection from: " + str(addr) )

msg = input("Message: ")
aes_text,salt,iv = encrypt(msg,key)
msg_encode = msg.encode() # Hashing requires unicode-objects to be encoded.
hsh_hmac = hmac.new(key.encode(),msg_encode,hashlib.sha512)

cnn.send(iv)
time.sleep(1)
cnn.send(salt)
time.sleep(1)
cnn.send(aes_text)
time.sleep(1)
cnn.send(hsh_hmac.hexdigest().encode()) # hexdigest() Returns the encoded data in hexadecimal format.
time.sleep(1)

node.close()
