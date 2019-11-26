## -*- coding: utf-8 -*-
#"""
#Spyder Editor
#
#This is a temporary script file.
#"""
#
#import socket
#
##AF_IFNET == ipv4
##SOCK_STREAM == TCP
#s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#s.bind((socket.gethostname(), 12345)) #tuple of hostname and portnumber
#s.listen(10) #a queue of 10 computers
##now we listen for connections
#input_command = input("Enter your command: ")
#print(input_command, type(input_command))
#b_com = bytes(input_command, 'utf-8')
#while True:
#    clientsocket, address = s.accept()
#    print(f"Connection from {address} has been established.")
#    #clientsocket.send(bytes("Hey there", "utf-8"))
#    clientsocket.send(b_com)
#    clientsocket.close()

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("121.0.0.50", 21))
#s.close()
#clientSocket.close()
#s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#as e server we need to bind the socket to the server port
#s.bind((socket.gethostname(), 12345))
#s.bind(("121.0.0.50", 21))
#our queue will be 5 PCs
s.listen(5)
clientSocket, address = s.accept()
print(f"Connection from {address} has been established")

stop_word = "quit"
stop_word = stop_word + '\r\n'
f = open("Yazaki.txt", "w")
#full_msg = ''
full_msg = '0'

while True:
    msg = clientSocket.recv(1024)
    print(msg.decode("utf-8"))
    full_msg = msg.decode("utf-8")

    if full_msg != '0':
        f = open("Yazaki.txt", "w")
        full_msg = full_msg.replace('\r\n', '')
        f.write(full_msg)
        f.close()
        full_msg = '0'
		
    if full_msg == stop_word:
        clientSocket.close()
        
