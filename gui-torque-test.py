# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 11:09:55 2020

@author: AMZ
"""

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


###### Adding 3 side by side Images#####################
im = Image.open("minion.jpg")
im = im.resize((450, 450), Image.ANTIALIAS)
img = ImageTk.PhotoImage(im)
img_lbl = Label(root, image=img)
img_lbl.pack(side=LEFT)



im2 = Image.open("panda.jpg")
im2 = im2.resize((450, 450), Image.ANTIALIAS)
img2 = ImageTk.PhotoImage(im2)
img2_lbl = Label(root, image=img2)
img2_lbl.pack(side=LEFT)

im3 = Image.open("pic.jpg")
im3 = im3.resize((450, 450), Image.ANTIALIAS)
img3 = ImageTk.PhotoImage(im3)
img3_lbl = Label(root, image=img3)
img3_lbl.pack(side=LEFT)

root.mainloop()
