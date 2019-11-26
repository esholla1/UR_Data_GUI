# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 15:56:05 2019

@author: 10493947
"""

#from tkinter import *
#
#class Window(Frame):
#    def __init__(self, master = None):
#        Frame.__init__(self, master)
#        
#        self.master = master
#        
#root = Tk()
#app = Window(root)
#root.mainloop()

############ Second Example #############################
#import tkinter as tk
#
#class Application(tk.Frame):
#    def __init__(self, master=None):
#        super().__init__(master)
#        self.master = master
#        self.pack()
#        self.create_widgets()
#        
#    def create_widgets(self):
#        self.hi_there = tk.Button(self)
#        self.hi_there["text"] = "Hello World\n (click me)"
#        self.hi_there["command"] = self.say_hi
#        self.hi_there.pack(side = "top")
#        
#        self.quit = tk.Button(self, text = "QUIT", fg = "red",
#                              command = self.master.destroy)
#        
#        self.quit.pack(side = "bottom")
#        
#    def say_hi(self):
#            print("hi there")
#
#root = tk.Tk()
#app = Application(master = root)
#app.mainloop()

#!/usr/bin/env python3

from tkinter import *
import socket

# ************* Socket Programming ***********************



#s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
##as e server we need to bind the socket to the server port
#s.bind((socket.gethostname(), 12345))
##our queue will be 5 PCs
#s.listen(5)
#clientSocket, address = s.accept()
#print(f"Connection from {address} has been established")
#
#stop_word = "quit"
#stop_word = stop_word + '\r\n'
#f = open("client_text.txt", "w")
#full_msg = ''
#
#while True:
#    msg = clientSocket.recv(1024)
#    print(msg.decode("utf-8"))
#    full_msg = msg.decode("utf-8")
#    if full_msg == stop_word:
#        clientSocket.close()
#        f.close()
#    f.write(full_msg)



# ************** Creation of GUI ************************
root = Tk()
root.title("UR-Gui")
root.geometry("190x200")

def close_window(): #when clicking the Quit button this fcn will get activated
    root.destroy()

ip_string_var = StringVar()
ip_string_var.set('271.0.0.50')
port_string_var = StringVar()
port_string_var.set('12345')
msg_string_var = StringVar()
msg_string_var.set('Hello')



YNA = Label(root, text="Yazaki North America", bg="red", fg="white")
YNA.pack(fill=X)
button2 = Button(text="Connected", fg="white", bg = "green")
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
button1 = Button(text="Quit",command = close_window, fg="red")
button1.pack()
#text = Text(root)
#text.insert(INSERT, "HELLO")
#text.pack()

root.mainloop()
