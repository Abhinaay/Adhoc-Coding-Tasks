#Problem : write a code that will take input from a user and check that if it is a command
#          then execute it with following  conditions :

# i)  all the commands given by user either wrong or right must be store in a file
#ii)   output of success command will be shown to monitor
#iii)  if the input command is repeated by user give him voice note not to do this again

import subprocess
from gtts import gTTS
import os
import win32com.client


osstdout=2
read =input("Enter : ")
#check for command correctness...
try:
            osstdout = subprocess.check_call(read.split())
except:
            a=2

speaker=win32com.client.Dispatch("SAPI.SpVoice")
if osstdout != 0 :
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

            #file = "file.mp3"

            # initialize tts, create mp3 and play
            #tts = gTTS(s, 'en')
            #tts.save(file)
            #os.system("mpg123 D:\\git-repos\\Python-Challenges-Adhoc\\" + file)
           
            
           

            
f.write("\n"+read) 
                    
    
 

