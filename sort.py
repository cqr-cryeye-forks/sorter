#python3
import os
import re
import sys
import numpy as np


def unique(list1):
	x = np.array(list1)
	sorted = np.unique(x)
	for value in sorted:
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
		for address, dirs, files in folder:
			for file in files:
				if type == 'f':
					all_files.append(address+'/'+file)
				elif type == 'd':
					all_directories.append(address+'/')
				else:
					print('Error in type format')
					exit()
	else:
		print('type is not f or d')
if type == 'f':
	unique(all_files)
#all_files = sorted(set(all_files))
#	for value in all_files:
#		print(value)
elif type == 'd':
	unique(all_directories)
#all_directories = sorted(set(all_directories))
#	for value in all_directories:
#		print(value)
else:
	exit()
