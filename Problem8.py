#Problem : write a code that will take input from a user and check that if it is a command
#          then execute it with following  conditions :

# i)  all the commands given by user either wrong or right must be store in a file
#ii)   output of success command will be shown to monitor
#iii)  if the input command is repeated by user give him voice note not to do this again

import subprocess
import win32com.client


out=2
read =input("Enter Command: ")
#check for command correctness...
try:
            out = subprocess.check_call(read.split())
except:
            a=2

speaker=win32com.client.Dispatch("SAPI.SpVoice")
if out != 0 :
    print('Command Not Found !!')
else :
    #If Command is correct ...
    f=open("cmdlist.txt",'r+')
    for i in f.readlines():
        print(i)
        if i == read :
            print("Don't repeat this command again....")
            
            s = "Don't repeat this command again...."
            speaker.Speak(s)

           

            
f.write("\n"+read) 
                    
    
 

