#!/usr/bin/python3

import  socket 
recv_ip="127.0.0.1"	#Enter Reciever IP		
recv_port=4444  		

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

while 4 >  3  :
	msg=input("Enter your message :   ")
	if msg == 'quit':
		exit()	
	if len(msg) <= 150 :
		nmsg=msg.encode()
		s.sendto(nmsg,(recv_ip,recv_port)) 
		reply=s.recvfrom(10)
		print("Msg from reciever : "+reply[0].decode())
	else :
		print("Error !!! Message must be less than 150 characters")
	
	

s.close()



