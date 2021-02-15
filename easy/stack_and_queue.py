#!/usr/bin/python3
n=int(input("Enter the number of items to be entered: "))
i=(input("Provide the space seperated items: "))
queue=i.split() #Splits the string into a list
stack=[]

print("\nRetriving items from the queue\n")
for q in range(n): #First in first out
	p=queue.pop(0)
	stack.append(p)
	print(p)

print("\nRetriving items from the stack\n")
for s in range(n):
	print(stack.pop()) #Last in last out
