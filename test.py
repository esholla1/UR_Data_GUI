# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 13:20:21 2019

@author: AMZ
"""

#input_command = input("Enter your command: ")
#print(input_command, type(input_command))
#print("hi")
#
#
#import torch
#
#x = torch.rand(3, 3)
#print(x)

f = open("test.txt", "w") #creating a text file so I can write into it
user_info = input("Enter the info you want to write in the file: ") #get user input
for i in range(4):
    f.write(user_info + '\n') #write user input to the text file and add a new line
f.close() #close text file

