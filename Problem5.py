#Problem : Write a code  will take  input as your name and greet you with
#	   good morning , good evening , goodafter noon , good night as per the current time your # 	   system.





#!/usr/bin/python3
import datetime

now=datetime.datetime.now()
name=input("Enter Your Name :")

if now.hour<12 and now.hour >3 :
	print("Good Morning!! ",name)
elif now.hour>=12 and now.hour<16 :
	print('Good Afternoon!! ',name)
elif now.hour >=16 and now.hour<21:
	print("Good Evening!! ",name)
elif now.hour >= 21 or now.hour <=3 :
	print("Good Night!! ",name)
