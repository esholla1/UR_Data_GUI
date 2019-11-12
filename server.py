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

