# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 08:39:28 2020

@author: AMZ
"""
from tkinter import *
from functools import partial
from PIL import Image, ImageTk

def close_window(s): #when clicking the Quit button this fcn will get activated
   #s.close()
    root.destroy()

s = '121.0.0.20'
root = Tk()
root.title("UR-Gui")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
dim = str(screen_width)+'x'+str(screen_height)
root.geometry(dim)
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

im = Image.open("smiley.jpg")
im = im.resize((250, 250), Image.ANTIALIAS)
smiley_img = ImageTk.PhotoImage(im)



smiley_lbl = Label(root, image=smiley_img)
smiley_lbl.pack(side = "bottom", fill = "both", expand="yes")
#clientSocket, address = s.accept()

root.mainloop()