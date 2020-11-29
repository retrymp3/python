#!/usr/bin/python3
n=int(input("Enter the number of items to be entered: "))
i=(input("Provide the space seperated items: "))
queue=i.split()
stack=[]

print("\nRetriving items from the queue\n")
for q in range(n):
	p=queue.pop(0)
	stack.append(p)
	print(p)

print("\nRetriving items from the stack\n")
for s in range(n):
	print(stack.pop())
