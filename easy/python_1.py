#!/usr/bin/python3

s = input("Enter the string: ")
k = int(input("Enter the key: "))

for i in s:
	if (ord(i) >= 97 and ord(i) <= 122):
		d = chr(((ord(i) + k)-97) %26 + 97) 
		print (d,end="")
	elif (ord(i)>=65 and ord(i)<=90):
		d= chr(((ord(i) + k)-65) %26 + 65)
		print (d,end="")
	elif (ord(i) >= 48 and ord(i) <= 57):
		d = chr(((ord(i) + k)-48) %26 + 48)
		print (d,end="")
print("")
