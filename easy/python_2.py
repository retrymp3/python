#!/usr/bin/python3
import os

#A python program that will list all the contents of directories using breadth first search
#dir1,dir2,dir3,etc are the names of directories
directory_tree = {
  'dir1' : ['dir2','dir3'],
  'dir2' : ['dir4', 'dir5'],
  'dir3' : ['dir6'],
  'dir4' : [],
  'dir5' : ['dir6'],
  'dir6' : []
}

explored = []
srh = []
x = str(input("Pick a directory from(dir1,dir2,dir3,dir4,dir5,dir6): "))

srh.append(x)
explored.append(x)

while srh:
	p = srh.pop(0)
#	change the path of the directory before using it in your own system
	cmd = "ls $HOME/Desktop/bi0s/pentest_team/tasks/python/easy/python_2/"+p
	os.system(cmd)
#	print(p)
	for i in directory_tree[p]:
		if i not in explored:
			explored.append(i)
			srh.append(i)
		
