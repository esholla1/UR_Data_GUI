# -*- coding: utf-8 -*-
from tkinter import *
from PIL import Image, ImageTk
import socket
import sys
from threading import Thread
from functools import partial

def close_window(s): #when clicking the Quit button this fcn will get activated
    s.close()
    root.destroy()
    sys.exit()

stop_word = "quit"
stop_word = stop_word + '\r\n'
globalfull_msg = '0'
full_msg = "0"
Status = "0"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Creation of 
s.bind(("121.0.0.20", 21))
#s.bind((socket.gethostname(), 12345))
s.listen(5)
def socket_connection():
    global Status
    global clientSocket
    global full_msg
    
    global path
    
    print("socket_connection 1")
    while True:
        path = ("C:/Yazaki/CODEBAR/images/")
        if  Status == "0":
            print('Waiting...')
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
            print("Waiting for data ... ")
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
            #f = open("Yazaki.txt", "a")
            full_msg = full_msg.replace('\r\n', '')
            
            if full_msg != "":
                print("this is full msg: " + full_msg)
                print("this is the first letter: " + full_msg[0])
                
    ####################### Changing the images, part numbers, messages and states as needed ##################################           
                
                if (full_msg[0] == 'A'):
                    print(full_msg[1:3])
                    #####  Changing Images  #######
                    if(full_msg[1:3] == "IM"):
                        if(full_msg[3:8] == "EMPTY"):
                            path = path + full_msg[3:8]
                            path = path + '.jpg'
                            im_a = Image.open(path)
                            im_a = im_a.resize((620, 700))
                            img_a = ImageTk.PhotoImage(im_a)
                            img_lbl.configure(image=img_a)
                            img_lbl.image = img_a
                            pn1_cb_sv.set('Not Checked')
                            l.config(bg="red")
                        else:
                            path = path + full_msg[3:6]
                            path = path + '.jpg'
                            im_a = Image.open(path)
                            im_a = im_a.resize((620, 700))
                            img_a = ImageTk.PhotoImage(im_a)
                            img_lbl.configure(image=img_a)
                            img_lbl.image = img_a
                            pn1_cb_sv.set('Checked')
                            l.config(bg="green")
                            
                            
                    #######  Changing the part number ###########
                    elif(full_msg[1:3] == "PN"):
                        pn1_sv.set(full_msg[3:])
                    #######  Changing the Message ##############
                    elif(full_msg[1:2] == "M"):
                        if(full_msg[2:3] == "1"):
                            msg1_sv_a.set(full_msg[3:])
                        if(full_msg[2:3] == "2"):
                            msg1_sv_b.set(full_msg[3:])
                        if(full_msg[2:3] == "3"):
                            msg1_sv_c.set(full_msg[3:])
                    elif (full_msg[1:3]) == "PR":
                        f = open("Yazaki.txt", "a")
                        full_msg = full_msg.replace('APR', '')
                        msg_string_var.set(full_msg)
                        f.write(full_msg)
                        f.close()
    
                
                if (full_msg[0] == 'B'):
                    print(full_msg[1:3])
                    #####  Changing Images  #######
                    if(full_msg[1:3] == "IM"):
                        if(full_msg[3:8] == "EMPTY"):
                            path = path + full_msg[3:8]
                            path = path + '.jpg'
                            im_a = Image.open(path)
                            im_a = im_a.resize((620, 700))
                            img_a = ImageTk.PhotoImage(im_a)
                            img2_lbl.configure(image=img_a)
                            img2_lbl.image = img_a
                            pn2_cb_sv.set('Not Checked')
                            m.config(bg="red")
                        else:
                            path = path + full_msg[3:6]
                            path = path + '.jpg'
                            im_a = Image.open(path)
                            im_a = im_a.resize((620, 700))
                            img_a = ImageTk.PhotoImage(im_a)
                            img2_lbl.configure(image=img_a)
                            img2_lbl.image = img_a
                            pn2_cb_sv.set('Checked')
                            m.config(bg="green")
                    #######  Changing the part number ###########
                    elif(full_msg[1:3] == "PN"):
                        pn2_sv.set(full_msg[3:])
                    #######  Changing the Message ##############
                    elif(full_msg[1:2] == "M"):
                        if(full_msg[2:3] == "1"):
                            msg2_sv_a.set(full_msg[3:])
                        if(full_msg[2:3] == "2"):
                            msg2_sv_b.set(full_msg[3:])
                        if(full_msg[2:3] == "3"):
                            msg2_sv_c.set(full_msg[3:])
                    elif (full_msg[1:3]) == "PR":
                        f = open("Yazaki.txt", "a")
                        full_msg = full_msg.replace('BPR', '')
                        msg_string_var.set(full_msg)
                        f.write(full_msg)
                        f.close()
                
                
                if (full_msg[0] == 'C'):
                    print(full_msg[1:3])
                    #####  Changing Images  #######
                    if(full_msg[1:3] == "IM"):
                        if(full_msg[3:8] == "EMPTY"):
                            path = path + full_msg[3:8]
                            path = path + '.jpg'
                            im_a = Image.open(path)
                            im_a = im_a.resize((620, 700))
                            img_a = ImageTk.PhotoImage(im_a)
                            img3_lbl.configure(image=img_a)
                            img3_lbl.image = img_a
                            pn3_cb_sv.set('Not Checked')
                            r.config(bg="red")
                        else:
                            path = path + full_msg[3:6]
                            path = path + '.jpg'
                            im_a = Image.open(path)
                            im_a = im_a.resize((620, 700))
                            img_a = ImageTk.PhotoImage(im_a)
                            img3_lbl.configure(image=img_a)
                            img3_lbl.image = img_a
                            pn3_cb_sv.set('Checked')
                            r.config(bg="green")
                    #######  Changing the part number ###########
                    elif(full_msg[1:3] == "PN"):
                        pn3_sv.set(full_msg[3:])
                    #######  Changing the Message ##############
                    elif(full_msg[1:2] == "M"):
                        if(full_msg[2:3] == "1"):
                            msg3_sv_a.set(full_msg[3:])
                        if(full_msg[2:3] == "2"):
                            msg3_sv_b.set(full_msg[3:])
                        if(full_msg[2:3] == "3"):
                            msg3_sv_c.set(full_msg[3:])
                
                
                    elif (full_msg[1:3]) == "PR":
                        f = open("Yazaki.txt", "a")
                        full_msg = full_msg.replace('CPR', '')
                        msg_string_var.set(full_msg)
                        f.write(full_msg)
                        f.close()
                
            full_msg = '0'                
    
    #root.after(100, socket_connection)

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
button2.pack(side = LEFT, padx = (790, 158))
button1 = Button(frame4, text="Quit",command = partial(close_window, s), fg="white", bg = "red")
button1.pack(side = LEFT)

frame5 = Frame(root, relief = RAISED, borderwidth = 2)
frame5.pack(fill= X)
ip = Label(frame5, text="IP Address")
ip.pack(side=LEFT, padx = 0)
entry1 = Entry(frame5, textvariable = ip_string_var)
entry1.pack(side=LEFT)
port = Label(frame5, text="Port Number")
entry2 = Entry(frame5, textvariable = port_string_var)
port.pack(side = LEFT, padx = (550, 0)) #We enter a tuple for padx to pad only on one side (left, right)
entry2.pack(side=LEFT)
message = Label(frame5, text = "Message")
message.pack(side=LEFT, padx = (550, 0))
entry3 = Entry(frame5, textvariable = msg_string_var)
entry3.pack(side=LEFT)




####################### Adding 3 side by side Image  #####################
pn1_sv = StringVar()
pn1_sv.set('PartNumber1')
pn2_sv = StringVar()
pn2_sv.set('PartNumber2')
pn3_sv = StringVar()
pn3_sv.set('PartNumber3')

frame1 = Frame(root, relief = RAISED, borderwidth = 2)
frame1.pack(fill = X)
l = Entry(frame1, textvariable=pn1_sv, bg = "OliveDrab1") #left
l.pack(side = LEFT, padx = 0, ipadx=230, ipady=10)
m = Entry(frame1, textvariable= pn2_sv, bg = "OliveDrab1") #middle
m.pack(side = LEFT, padx = 43, ipadx = 230, ipady=10)
r = Entry(frame1, textvariable=pn3_sv, bg = "OliveDrab1")  #right
r.pack(side = LEFT, padx =0, ipadx=230, ipady=10) 

frame2 = Frame(root, relief=RAISED, borderwidth = 2)
frame2.pack(fill = X)
epath = ("C:/Yazaki/CODEBAR/images/")
epath = epath + ("EMPTY.jpg")

im = Image.open(epath)
im = im.resize((620, 700), Image.ANTIALIAS)
img = ImageTk.PhotoImage(im)
img_lbl = Label(frame2, image=img)
img_lbl.pack(side=LEFT)

im2 = Image.open(epath)
im2 = im2.resize((620, 700), Image.ANTIALIAS)
img2 = ImageTk.PhotoImage(im2)
img2_lbl = Label(frame2, image=img2)
img2_lbl.pack(side=LEFT)

im3 = Image.open(epath)
im3 = im3.resize((620, 700), Image.ANTIALIAS)
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
l = Entry(frame3, textvariable=pn1_cb_sv, bg = "red", fg = "white")
l.pack(side = LEFT, padx = 0)
m = Entry(frame3, textvariable=pn2_cb_sv, bg = "red", fg = "white")
m.pack(side = LEFT, padx = 500)
r = Entry(frame3, textvariable=pn3_cb_sv, bg = "red", fg = "white")
r.pack(side = LEFT, padx =0)


########################## Adding the three message sections ##################
msg1_sv_a = StringVar()
msg1_sv_a.set('MessageA1')
msg2_sv_a = StringVar()
msg2_sv_a.set('MessageB1')
msg3_sv_a = StringVar()
msg3_sv_a.set('MessageC1')

msg1_sv_b = StringVar()
msg1_sv_b.set('MessageA2')
msg2_sv_b = StringVar()
msg2_sv_b.set('MessageB2')
msg3_sv_b = StringVar()
msg3_sv_b.set('MessageC2')

msg1_sv_c = StringVar()
msg1_sv_c.set('MessageA3')
msg2_sv_c = StringVar()
msg2_sv_c.set('MessageB3')
msg3_sv_c = StringVar()
msg3_sv_c.set('MessageC3')

frame_msg_a = Frame(root, relief = RAISED, borderwidth = 1)
frame_msg_a.pack(fill = X, pady = 1)
msg1_a = Label(frame_msg_a, text = "Message1", bg = "RoyalBlue1")
msg1_a.pack(side = LEFT, ipady = 10)
entry_msg1_a = Entry(frame_msg_a, textvariable = msg1_sv_a)
entry_msg1_a.pack(ipadx= 200, ipady = 10, side=LEFT)
msg2_a = Label(frame_msg_a, text = "Message1", bg = "RoyalBlue1")
msg2_a.pack(side = LEFT, padx = (43, 0), ipady = 10)
entry_msg2_a = Entry(frame_msg_a, textvariable = msg2_sv_a)
entry_msg2_a.pack(ipadx=200, ipady=10, side = LEFT)
msg3_a = Label(frame_msg_a, text = "Message1", bg = "RoyalBlue1")
msg3_a.pack(side = LEFT, padx = (43, 0), ipady = 10)
entry_msg3_a = Entry(frame_msg_a, textvariable = msg3_sv_a)
entry_msg3_a.pack(ipadx=200, ipady=10, side = LEFT)



frame_msg_b = Frame(root, relief = RAISED, borderwidth = 1)
frame_msg_b.pack(fill = X, pady = 1)
msg1_b = Label(frame_msg_b, text = "Message2", bg = "RoyalBlue1")
msg1_b.pack(side = LEFT, ipady = 10)
entry_msg1_b = Entry(frame_msg_b, textvariable = msg1_sv_b)
entry_msg1_b.pack(side = LEFT, ipadx= 200, ipady = 10)
msg2_b = Label(frame_msg_b, text = "Message2", bg = "RoyalBlue1")
msg2_b.pack(side = LEFT, padx = (43, 0), ipady = 10)
entry_msg2_b = Entry(frame_msg_b, textvariable = msg2_sv_b)
entry_msg2_b.pack(side = LEFT, ipadx= 200, ipady = 10)
msg3_b = Label(frame_msg_b, text = "Message2", bg = "RoyalBlue1")
msg3_b.pack(side = LEFT, padx=(43, 0), ipady = 10)
entry_msg3_b = Entry(frame_msg_b, textvariable = msg3_sv_b)
entry_msg3_b.pack(side = LEFT, ipadx= 200, ipady = 10)

frame_msg_c = Frame(root, relief = RAISED, borderwidth = 1)
frame_msg_c.pack(fill = X, pady = 1)
msg1_c = Label(frame_msg_c, text = "Message3", bg = "RoyalBlue1")
msg1_c.pack(side = LEFT, ipady = 10)
entry_msg1_c = Entry(frame_msg_c, textvariable = msg1_sv_c)
entry_msg1_c.pack(side = LEFT, ipadx= 200, ipady = 10)
msg2_c = Label(frame_msg_c, text = "Message3", bg = "RoyalBlue1")
msg2_c.pack(side = LEFT, padx = (43, 0), ipady = 10)
entry_msg2_c = Entry(frame_msg_c, textvariable = msg2_sv_c)
entry_msg2_c.pack(side = LEFT, ipadx= 200, ipady = 10)
msg3_c = Label(frame_msg_c, text = "Message3", bg = "RoyalBlue1")
msg3_c.pack(side = LEFT, padx = (43, 0), ipady = 10)
entry_msg3_c = Entry(frame_msg_c, textvariable = msg3_sv_c)
entry_msg3_c.pack(side = LEFT, ipadx= 200, ipady = 10)


x = Thread(target=socket_connection)
x.daemon = True
x.start()
#root.after(100, socket_connection)
root.mainloop()
