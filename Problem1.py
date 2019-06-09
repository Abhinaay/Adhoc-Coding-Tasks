#Problem:Create a program that asks the user to enter their name and their age.
#        Print out a message that will tell them the year that they will turn 95 years old.



#!/usr/bin/python3
from datetime import date

name=input("Enter Your Name : ")
age=int(input("Enter Your Age : "))


print("Hi %s, you will be 95 years old in the year : "%name,(date.today().year+95-age))


