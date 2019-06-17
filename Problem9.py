#Problem : write a code that will take user input until number of character not exceeding
#	   500 chars.

#Now do the following  tasks:
#i)   print the number of repeated characters in descending order
#ii)  print number of repeated words in descending order
#iii)  if a word is repeating more than 5 times remove all those words
#iv)  if a word is present only one times add the same word in that string but length must not #increase more than 500 chars , you can remove any random thing for doing the same .

#!/usr/bin/python3
import getch
import operator
import textwrap

s=""
j=0
for i in range(500):
	s+=getch.getch()
sorted_dict1=dict()
sorted_dict2=dict()	
dict1=dict()
dict2=dict()
def freqword(str): 
	# break the string into list of words  
	str = str.split()          
	str2 = [] 
	
	# loop till string values present in list str 
	for i in str:              
		# checking for the duplicacy 
		if i not in str2: 
		        str2.append(i)  
	    # count the frequency of each word          
	for i in range(0, len(str2)):
		dict1[str2[i]]=str.count(str2[i])
	sorted_dict1 = sorted(dict1.items(), key=operator.itemgetter(1),reverse=True)
	print('\nFrequency of words in descending order :\n ')
	print(sorted_dict1)

def freqchar(str):
	# break the string into char
	str2 = list(str)
	#print(str2)
	str3=[]
	
	for i in str2:              
		# checking for the duplicacy 
		if i not in str3: 
		        str3.append(i)  
	    # count the frequency of each word          
	for i in range(0, len(str3)):
		#print('Frequency of', str3[i], 'is :', str.count(str3[i]),'\n')     
	        dict2[str3[i]]=str.count(str3[i])
	sorted_dict2 = sorted(dict2.items(), key=operator.itemgetter(1),reverse=True)
	print('\nFrequency of characters in descending order :\n ')
	print(sorted_dict2)     

freqchar(s)	
freqword(s)

for i in dict1 :
	if dict1.get(i) >= 5 :
		k=s.replace(i,'')
		s=k
	elif dict1.get(i) == 1 :
		s+=' '+i
	else:
		kk=0



print('\nFinal String : \n',textwrap.shorten(s,width=500,placeholder=''))
