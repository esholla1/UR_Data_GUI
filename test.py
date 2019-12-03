# -*- coding: utf-8 -*-
"""
@author: Elis Sholla
"""
from tkinter import *
import socket
from functools import partial
# ************** Creation of GUI ************************
def close_window(s): #when clicking the Quit button this fcn will get activated
    s.close()
    root.destroy()

root = Tk()
root.title("UR-Gui")
root.geometry("190x200")



s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#s.bind(("121.0.0.50", 21))
s.bind((socket.gethostname(), 12345))
#our queue will be 5 PCs
s.listen(5)
clientSocket, address = s.accept()
ip = address[0]
port = address[1]
print(ip, type(ip)) #ip type --> string
print(f"Connection from {address} has been established")



ip_string_var = StringVar()
#ip_string_var.set('271.0.0.50')
ip_string_var.set(ip)
port_string_var = StringVar()
#port_string_var.set('12345')
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
button1 = Button(text="Quit",command = partial(close_window, s), fg="red")
button1.pack()
#text = Text(root)
#text.insert(INSERT, "HELLO")
#text.pack()
root.mainloop()

stop_word = "quit"
stop_word = stop_word + '\r\n'
f = open("Yazaki.txt", "w")
#full_msg = ''
full_msg = '0'

while True:
    msg = clientSocket.recv(1024)
    print(msg.decode("utf-8"))
    full_msg = msg.decode("utf-8")

    if full_msg == stop_word:
        clientSocket.close()
        f.close()
        break

    if full_msg != '0':
        f = open("Yazaki.txt", "a")
        full_msg = full_msg.replace('\r\n', '')
        msg_string_var.set(full_msg)
        f.write(full_msg)
        f.close()
        full_msg = '0'
