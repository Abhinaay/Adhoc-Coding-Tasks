# Problem : use file handling to create a linux command  similar to cat .
#  		test at least  4 cases and options of cat command.


#!/usr/bin/python3

import sys

#list1= sys.argv





try: 
	if len(sys.argv) == 2:
		if sys.argv[1] == '--help' :
			print("This command is similar to cat command and has its 5 features similar to that.\nWe can create a file using syntax :\n   p > filename)\nWe can view help using syntax :\n   p --help\nWe can view a file using syntax :")
			print("   p <filename>\nWe can overwrite a file using syntax :\n   p (file name to read from) > (filename)\nWe can append a file using syntax :\n   p (file name to read from ) >> (filename)\n")
		else :
			f = open(sys.argv[1])
			print(f.read())
			f.close()
	elif len(sys.argv) == 3:
		if sys.argv[1] == '>':
			a=2
	
	elif len(sys.argv) == 4:
		if sys.argv[2]=='>':
			f1 = open(sys.argv[1],'r+')
			f2 = open(sys.argv[3],'w+')
			text=f1.read()
			f2.write(text)	
			f1.close()
			f2.close()
		elif sys.argv[2]=='>>':
			f1 = open(sys.argv[1],'r+')
			f2 = open(sys.argv[3],'a+')
			text=f1.read()
			f2.write(text)	
			f1.close()
			f2.close()
		else:
			a=2
	else:
		"Wrong Syntax!!!! See help.."
except: 
	print('Wrong Syntax!!!! See help..')

