#!/usr/bin/python3

import  socket 

recv_ip="127.0.0.1"	#Enter reciever IP
recv_port=4444  

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind((recv_ip,recv_port))

while  True  :
	data=s.recvfrom(100)  
	ndata=data[0].decode()
	print("Message  from sender  ",ndata)

	#  reply to sender  
	rply=input("Type your reply  : ")
	s.sendto(rply.encode(),data[1])


s.close()
