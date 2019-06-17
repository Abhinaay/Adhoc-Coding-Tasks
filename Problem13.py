import pyttsx3
import datetime
import os
import sys

engine = pyttsx3.init()
voices = engine.getProperty('voices')         
engine.setProperty('voice', voices[1].id)   

engine.say("Aur Bhhatt  sahaab !! ki haal hai ")

now=datetime.datetime.now()
if now.hour<12 and now.hour >3 :
    engine.say("Good Morning biddu")
elif now.hour>=12 and now.hour<16 :
    engine.say('Good Afternoon!! baahar bahot dhooop hai')
elif now.hour >=16 and now.hour<21:
    engine.say("Good Evening!! chai peogai?")
elif now.hour >= 21 or now.hour <=3 :
    engine.say("soja bae!! kab tak jagaega")

engine.say("I can add numbers for you!")
engine.say("I can also sort numbers!")
engine.say("I can also print number of installed modules!")

def add(*argv):
    sum=0
    for arg in argv:
        sum=sum+arg
    print(sum)

def sort(*argv):
    list1=[]
    for arg in argv:
        list1.append(arg)
    list1.sort()
    for i in list1:
        print(i)

def listModules():
    os.system("pip freeze | wc -l | cat > list.txt")
    f=open("list.txt","r+")
    print(f.read())


engine.runAndWait()
