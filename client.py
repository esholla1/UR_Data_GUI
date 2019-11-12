# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 10:55:18 2019

@author: AMZ
"""
#name = input("Enter a name: ")
#print(name)

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#Since this is client, we are going to try to connect
#s.connect(("121.0.0.10", 12345))
s.connect(("192.168.68.26", 12345))
full_msg = '' #received message
#message = ""
#message = input('-->') #message that we will be sending

#adding all the received data to a text file
f = open("server_data.txt", "w")
count = 1
while count == 1:
    msg = s.recv(1024)
#    if len(msg) <= 0:
#        break
    full_msg = msg.decode('utf-8')
    f.write(full_msg + '\n')
    #s.send(b_com)
    print("Server: " + full_msg)
    if full_msg == "quit":
        count = 0
#    message = input('-->')
#    
#    if message == "quit":
#        break
#    if len(message) <= 0:
#        continue
#     s.send(message.encode('utf-8'))
    s.send(full_msg.encode('utf-8'))
f.close()
s.close()


