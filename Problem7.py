#Problem : use deep analysis of file handling to create a linux command similar to touch


#!/usr/bin/python3

import os
import sys
import time
from stat import *

#Take file name as input
file1 = input('Enter File Path Or Name : ')
check=os.path.exists(file1)
if check == False:
	if sys.argv[1] == '-c':
		exit()
	else:
		f=open(file1,'w+')
		f.close()
else:
	st = os.stat(file1)
	atime = st[ST_ATIME] #access time
	mtime = st[ST_MTIME] #modification time
	if sys.argv[1] == '-a':
		new_atime = time.time()
		os.utime(file1,(new_atime,mtime))
	elif sys.argv[1] == '-d':
		new_atime = time.time()
		new_mtime = time.time()
		os.utime(file1,(new_atime,new_mtime))
	elif sys.argv[1] == '-m':
		new_mtime = time.time()
		os.utime(file1,(atime,new_mtime))
	elif sys.argv[1] == '-c':
		new_atime = time.time()
		new_mtime = time.time()
		os.utime(file1,(new_atime,new_mtime))
	elif sys.argv[1] == '-r':
		st1 = os.stat(sys.argv[2])
		atime1 = st1[ST_ATIME] 
		mtime1 = st1[ST_MTIME]
		os.utime(file1,(atime1,mtime1))
	else:
		print("\n-------------Help-------------\n-a, change the access time only\n-c, if the file does not exist, do not create it\n-d, update the access and modification times\n-m, change the modification time only\n-r, use the access and modification times of file\n")

