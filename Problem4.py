#Problem : take all input from user .

#	i)  check that all character are string
#	ii)  if all char are string then create user in your linux based OS
#	iii)  also create password for same use,
#	      password will be  ===>>     hello{username}



#!/usr/bin/python3

import os

username=input("Enter the name of user you want to create : ")	
try:
	val = int(username)
	print("All characters are not string!!\nUser can't be created....")

except ValueError:
	print("All characters are string!!\n")
	os.system("adduser -p hello"+username+" "+username)
	print("User Created With username : "+username+" and password : hello"+username)




