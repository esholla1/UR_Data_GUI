# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 14:57:11 2019

@author: AMZ
"""


# -*- coding: utf-8 -*-

"""

@author: Elis Sholla

"""

from tkinter import *

import socket

from functools import partial

def close_window(s): #when clicking the Quit button this fcn will get activated
    s.close()
    root.destroy()

stop_word = "quit"
stop_word = stop_word + '\r\n'
globalfull_msg = '0'
full_msg = "0"
Status = "0"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Creation of 
s.bind(("121.0.0.20", 21))
s.listen(5)



def socket_connection():
    global Status
    global clientSocket
    global full_msg
    
    
    print("socket_connection 1")
    if  Status == "0":
        clientSocket, address = s.accept()
        print("socket_connection 2")
        print(address[0])
        print(address[1])
        ip_string_var.set(address[0])
        port_string_var.set(address[1])
        connected_sv.set("Connected")
        Status = "1"
#        
#        msg = clientSocket.recv(1024)
#        print(msg.decode("utf-8"))
#        full_msg = msg.decode("utf-8")
#        print("Full_msg 1",full_msg)
        
    else:
        print("Espera datos por segunda vez")
        msg = clientSocket.recv(1024)
        print(msg.decode("utf-8"))
        full_msg = msg.decode("utf-8")
        print("Full_msg 2",full_msg)
        
        if full_msg == "":
            print("Desconectado") 
            connected_sv.set("Not Connected")
            Status = "0"
   
    
    if full_msg == stop_word:
        clientSocket.close()
        f.close()
        #break
    
    if full_msg != '0':
        f = open("Yazaki.txt", "a")
        full_msg = full_msg.replace('\r\n', '')
        msg_string_var.set(full_msg)
        f.write(full_msg)
        f.close()
        full_msg = '0'
                

    root.after(100, socket_connection)



# ************** Creation of GUI ************************


root = Tk()
root.title("UR-Gui")
root.geometry("190x200")
address = (0, 0)
ip = address[0]
port = address[1]

print(ip, type(ip)) #ip type --> string

print(f"Connection from {address} has been established")

ip_string_var = StringVar()
ip_string_var.set(ip)
port_string_var = StringVar()   
port_string_var.set(port)
msg_string_var = StringVar()
msg_string_var.set('Hello')
connected_sv = StringVar()
connected_sv.set("Not Connected")
YNA = Label(root, text="Yazaki North America", bg="red", fg="white")
YNA.pack(fill=X)
button2 = Button(textvariable=connected_sv, fg="white", bg = "green")
button2.pack()
ip = Label(root, text="IP Address")
ip.pack()
entry1 = Entry(root, textvariable = ip_string_var)
entry1.pack()
port = Label(root, text="Port Number")
entry2 = Entry(root, textvariable = port_string_var)
port.pack()
entry2.pack()
message = Label(root, text = "Message")
message.pack()
entry3 = Entry(root, textvariable = msg_string_var)
entry3.pack()
button1 = Button(text="Quit",command = partial(close_window, s), fg="red")
button1.pack()

#clientSocket, address = s.accept()

root.after(100, socket_connection)
root.mainloop()

        
