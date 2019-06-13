#!/usr/bin/python2

import  socket 
import threading


def send():
    ip1="127.0.0.1"
    port1=5555
    s1=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    s1.bind((ip1,port1))
    while True:
        msg = input('\nMsg to Send >> ')
        s1.sendto(msg.encode(),(ip1,7777))

def receive():
    ip2="127.0.0.1"
    port2=9999
	
    s2=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    s2.bind((ip2,port2))
    while True:
        data = s2.recvfrom(100)
        print('\nMsg From Sender :: '+ data[0].decode())

if __name__ == "__main__":
  
	start=input("\nPress 1 for sending / receiving  text messages from both the side\nPress 2  sending file from sender and receiving from receiver\n")
	if start == '1' :

		thread_send = threading.Thread(target = send)
		thread_send.start()
		
		thread_receive = threading.Thread(target = receive)
		thread_receive.start()
	elif start == '2' :
		ip2="127.0.0.1"
		port2=9999
			
		s2=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
		s2.bind((ip2,port2))
		while True:
			data = s2.recvfrom(100)
			print('\nMsg From Sender :: '+ data[0].decode())
	else :
		print("Try Again!!!")
	

