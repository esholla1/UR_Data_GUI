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

root = Tk()
root.title("UR-Gui")
root.geometry("190x200")




button2 = Button(text="Connect", fg="green")
button2.pack()

YNA = Label(root, text="Yazaki North America", bg="red", fg="white")
YNA.pack(fill=X)

ip = Label(root, text="IP Address")
ip.pack()
entry1 = Entry(root)
entry1.pack()
port = Label(root, text="Port Number")
entry2 = Entry(root)
port.pack()
entry2.pack()
message = Label(root, text = "Message")
message.pack()
entry3 = Entry(root)
entry3.pack()

button1 = Button(text="Quit", fg="red")
button1.pack()
root.mainloop()

