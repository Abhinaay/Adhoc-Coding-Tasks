#Problem : write a code using  that will take user input from and search on google and store top 10 url in the list.
#               conditions : 
#               i )   URL must be stored permanently as well
#               ii)   user can give input using keyboard and  voice both



import speech_recognition as sr
from googlesearch import search

#choose mode of input
print("Enter Your Search Query : ")
mode=input("Press 1 to Speak...\nPress 2 to Write\n")
if mode=='1':
        r=sr.Recognizer()

        with sr.Microphone() as source:
                print("Listening....");
                audio=r.listen(source)
                print("Searching Your Query....")
                try:
                        data=r.recognize_google(audio)
                except:
                        pass;
elif mode=='2':
        data=input("Type : ")
else :
        print("Invalid Mode Selection")
        exit

mylist=[]
#Searching on google and appending to a list to save permanently
for i in search(data,stop=10):
        print(i)
        mylist.append(i)

print("\nThe result is stored in a list as shown below....\n")
print(mylist)
