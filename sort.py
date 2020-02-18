#python3
import os
import re
import sys
import numpy as np


def unique(list1):
	x = np.array(list1)
	sorted = np.unique(x)
	for value in sorted:
		value = value.split(sys.argv[2],1)
		value = str(value[1])
		if value.find('//'):
			value = value.replace('//','/')
		if value.startswith('/'):
			value = value[1:]
		if value.startswith('./'):
			value = value[2:]
		if len(value) > 0 and value != 0:
			print(value)
all_directories = []
all_files = []
if len (sys.argv) < 3:
	print ("Error, not enough parameters")
	sys.exit (1)
elif len (sys.argv) > 3:
	print ("Error, too many options")
	sys.exit (1)
else:
	type = sys.argv[1]
	dir = sys.argv[2]
	if type == 'f' or type == 'd':
		folder = []
		for i in os.walk(dir):
			folder.append(i)
		if type == 'd':
			for address, dirs, files in folder:
				all_directories.append(address+'/')
		elif type == 'f':
			for address, dirs, files in folder:
				for file in files:
					all_files.append(address+'/'+file)
		else:
			print('Error in type format')
			exit()
	else:
		print('type is not f or d')

if type == 'f':
	unique(all_files)
elif type == 'd':
	unique(all_directories)
else:
	exit()
