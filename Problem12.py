#!/usr/bin/python3

from googlesearch import search
import os


data=input("Type : ")
link=[]

for i in search(data,stop=3):
	print(i)
	link.append(i)
os.system("qrencode -s 16x16 -o /var/www/html/link1.png "+link[0])
os.system("qrencode -s 16x16 -o /var/www/html/link2.png "+link[1])
os.system("qrencode -s 16x16 -o /var/www/html/link3.png "+link[2])



