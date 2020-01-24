# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 13:00:53 2020

@author: AMZ
"""

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
from PIL import Image, ImageTk
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
#s.bind(("121.0.0.20", 21))
s.bind((socket.gethostname(), 12345))
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
        button2.config(bg="green")
        Status = "1"
#       
        
        
    else:
        print("Espera datos por segunda vez")
        msg = clientSocket.recv(1024)
        print(msg.decode("utf-8"))
        full_msg = msg.decode("utf-8")
        print("Full_msg 2",full_msg)
        
        if full_msg == "":
            print("Desconectado") 
            connected_sv.set("Not Connected")
            
            button2.config(bg="red")
            
            Status = "0"
   
    
    if full_msg == stop_word:
        clientSocket.close()
        f.close()
        #break
    
    if full_msg != '0':
        f = open("Yazaki.txt", "a")
        full_msg = full_msg.replace('\r\n', '')
        
        if full_msg != "":
            print("this is full msg: " + full_msg)
            print("this is the first letter: " + full_msg[0])
            
####################### Changing the images, Part numbers, and states as needed ##################################           
            
            if (full_msg[0] == 'A'):
                print(full_msg[1:3])
                if(full_msg[1:3] == "PN"):
                    pn1_sv.set(full_msg[3:8])
                    im_a = Image.open("earth.jpg")
                    im_a = im_a.resize((450, 400))
                    img_a = ImageTk.PhotoImage(im_a)
                    img_lbl.configure(image=img_a)
                    img_lbl.image = img_a
                    pn1_cb_sv.set('Checked')
                    l.config(bg="green")
                    
            if (full_msg[0] == 'B'):
                print(full_msg[1:3])
                if(full_msg[1:3] == "PN"):
                    pn2_sv.set(full_msg[3:8])
                    im_a = Image.open("eagle.jpg")
                    im_a = im_a.resize((450, 400))
                    img_a = ImageTk.PhotoImage(im_a)
                    img2_lbl.configure(image=img_a)
                    img2_lbl.image = img_a
                    pn2_cb_sv.set('Checked')
                    m.config(bg="green")
            
            if (full_msg[0] == 'C'):
                print(full_msg[1:3])
                if(full_msg[1:3] == "PN"):
                    pn3_sv.set(full_msg[3:8])
                    im_a = Image.open("uom.jpg")
                    im_a = im_a.resize((450, 400))
                    img_a = ImageTk.PhotoImage(im_a)
                    img3_lbl.configure(image=img_a)
                    img3_lbl.image = img_a
                    pn3_cb_sv.set('Checked')
                    r.config(bg = "green")
                    
        msg_string_var.set(full_msg)
        f.write(full_msg)
        
#        if full_msg[0] == "p":
#            im = Image.open("panda.jpg")
#            im = im.resize((250, 250), Image.ANTIALIAS)
#            smiley_img = ImageTk.PhotoImage(im)
#
#            smiley_lbl.configure(image=smiley_img)
#            smiley_lbl.image=smiley_img
        
        f.close()
        
#        if full_msg == "hi":

        
        
        full_msg = '0'
                

    root.after(5000, socket_connection)



# ************** Creation of GUI ************************


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

frame4 = Frame(root, relief = RAISED, borderwidth = 2)
frame4.pack(fill = X)
connected_sv.set("Not Connected")
YNA = Label(frame4, text="Yazaki North America", bg="red", fg="white")
YNA.pack(fill=X)
button2 = Button(frame4, textvariable=connected_sv, fg="white", bg = "red")
button2.pack()

frame5 = Frame(root, relief = RAISED, borderwidth = 2)
frame5.pack(fill= X)
ip = Label(frame5, text="IP Address")
ip.pack(side=LEFT, padx = 0)
entry1 = Entry(frame5, textvariable = ip_string_var)
entry1.pack(side=LEFT, padx = 0)
port = Label(frame5, text="Port Number")
entry2 = Entry(frame5, textvariable = port_string_var)
port.pack(side = LEFT, padx = (250, 0)) #We enter a tuple for padx to pad only on one side (left, right)
entry2.pack(side=LEFT)
message = Label(frame5, text = "Message")
message.pack(side=LEFT, padx = (250, 0))
entry3 = Entry(frame5, textvariable = msg_string_var)
entry3.pack(side=LEFT)

button1 = Button(text="Quit",command = partial(close_window, s), fg="red")
button1.pack()


####################### Adding 3 side by side Image  #####################

pn1_sv = StringVar()
pn1_sv.set('PartNumber1')
pn2_sv = StringVar()
pn2_sv.set('PartNumber2')
pn3_sv = StringVar()
pn3_sv.set('PartNumber3')


frame1 = Frame(root, relief = RAISED, borderwidth = 2)
frame1.pack(fill = X)
l = Label(frame1, textvariable=pn1_sv, bg = "orange") #left
l.pack(side = LEFT, padx = 0)
m = Label(frame1, textvariable= pn2_sv, bg = "orange") #middle
m.pack(side = LEFT, padx = 425)
r = Label(frame1, textvariable=pn3_sv, bg = "orange")  #right
r.pack(side = LEFT, padx =0) 


frame2 = Frame(root, relief=RAISED, borderwidth = 2)
frame2.pack(fill = X)

im = Image.open("minion.jpg")
im = im.resize((450, 400), Image.ANTIALIAS)
img = ImageTk.PhotoImage(im)
img_lbl = Label(frame2, image=img)
img_lbl.pack(side=LEFT)

im2 = Image.open("panda.jpg")
im2 = im2.resize((450, 400), Image.ANTIALIAS)
img2 = ImageTk.PhotoImage(im2)
img2_lbl = Label(frame2, image=img2)
img2_lbl.pack(side=LEFT)

im3 = Image.open("pic.jpg")
im3 = im3.resize((450, 400), Image.ANTIALIAS)
img3 = ImageTk.PhotoImage(im3)
img3_lbl = Label(frame2, image=img3)
img3_lbl.pack(side=LEFT)


pn1_cb_sv = StringVar()  #part number 1 check box string variable
pn1_cb_sv.set('Not Checked')
pn2_cb_sv = StringVar()
pn2_cb_sv.set('Not Checked')
pn3_cb_sv = StringVar()
pn3_cb_sv.set('Not Checked')


frame3 = Frame(root, relief = RAISED, borderwidth = 2)
frame3.pack(fill = X)
l = Label(frame3, textvariable=pn1_cb_sv, bg = "red", fg = "white")
l.pack(side = LEFT, padx = 0)
m = Label(frame3, textvariable=pn2_cb_sv, bg = "red", fg = "white")
m.pack(side = LEFT, padx = 425)
r = Label(frame3, textvariable=pn3_cb_sv, bg = "red", fg = "white")
r.pack(side = LEFT, padx =0)



#clientSocket, address = s.accept()

root.after(5000, socket_connection)
root.mainloop()

