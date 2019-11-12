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
f = open("server_data.txt", "w")

stop_word = "quit"
stop_word = stop_word + '\r\n' #adding '\r\n' to account for the .decode part of the str

while True:
   
    msg = s.recv(1024)
    full_msg = msg.decode('utf-8')
    
    if full_msg == stop_word: #if the server gives us the command quit
        break
    
    f.write(full_msg)
    #s.send(b_com)
    print("Server: " + full_msg)
    s.send(full_msg.encode('utf-8'))


f.close()
s.close()


