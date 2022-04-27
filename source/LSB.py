#!/usr/bin/env python3

import PIL.Image
from PIL import ImageTk
from tkinter import *


def message_to_bits(data):          ### for encoding
    newdata = []
    newdata = ''.join([format(ord(i), "08b") for i in data])
    return newdata

def image_to_pixel(image):          #converts images to pixel and returns pixel values 
    pixel=image.load()
    pixel_list = []
    for i in range(image.size[1]):
        for j in range(image.size[0]):
             pixel_list =pixel_list + list(pixel[j,i])
    
    return pixel_list

def modified_pixel(img,data): 
    datalist=message_to_bits(data)
    len_data = len(datalist)
    
    pixel = list(img.getdata())
    total_pixel = len(pixel)

    if(total_pixel<len_data):
        print("ERROR : Need more P1xels")
    else :
        counter =0
        for x in range(total_pixel):
            pseudo = list(pixel[x])
            for y in range(0,3):
                if counter < len_data:
                    pseudo[y] = int(bin(pseudo[y])[2:9]+datalist[counter],2)
                    counter +=1
            pixel[x]=tuple(pseudo)

    return(pixel)
    
def modif_encoded_image(pseudo_img,data):
    wd,ht = pseudo_img.size
        
    pixel = modified_pixel(pseudo_img,data)
    for x in range(wd):
        for y in range(ht):
            pseudo_img.putpixel((x,y),pixel[(y*wd+x)])    
    
def lsb_encode_image(img_path,message_input,save_path,frame):
    data = message_input.get(1.0,"end-1c")
    path_to_save_file = save_path.get(1.0,"end-1c")
    
    if(len(img_path)==0):
        L4 = Label(frame,text = "No Audio File Selected")
        L4.config(font = ("Times New Roman",12))
        L4.place(relx = 0.2,rely =0.5,anchor =CENTER)
    elif(len(data) == 0):
        L4 = Label(frame,text = "No Message Entered \n Enter the Message to Hide")
        L4.config(font = ("Times New Roman",12))
        L4.place(relx = 0.5,rely =0.5,anchor =CENTER)
    elif(len(path_to_save_file)==0):
        L5 = Label(frame,text = "Enter the file name \nto save the encoded file \nto procedd")
        L5.config(font = ("Times New Roman",12))
        L5.place(relx=0.8,rely=0.35,anchor=CENTER)
    else:
        image = PIL.Image.open(img_path,'r')
        image = image.convert("RGB")
        # need to check the above line
        data = data + "$t3g0"

        pseudo_img = image.copy()
        modif_encoded_image(pseudo_img,data)

        pseudo_img.save(path_to_save_file,str(path_to_save_file.split('.')[1].upper()))
        enc_mess = Label(frame,text = "Message Hiding: Success\n Image Saved: Success")
        enc_mess.config(font = ("Times New Romar",11))
        enc_mess.place(relx = 0.8,rely = 0.55,anchor = CENTER)

    x = PIL.Image.open(path_to_save_file)
    wd,ht = x.size
    if(wd>ht):
        factor = 200/wd
        wd = 200
        ht = int(ht*factor)
    elif(ht>wd):
        factor = 200/wd
        ht = 200
        wd = int(wd*factor)
    else:
        wd = 200
        ht = 200
    x = x.resize((wd,ht))
    img = ImageTk.PhotoImage(x)
    label =Label(frame, image=img)        
    label.image =img
    label.place(anchor=CENTER,relx =0.8,rely =0.33)


def lsb_decode_image(img_path,frame):
    message = ''

    image = PIL.Image.open(img_path,'r')
    pixel = list(image.getdata())
    total_pixel = len(pixel)

    hidden_bits =''
    for x in range(total_pixel):
        pseudo = list(pixel[x])
        for y in range(3):
            hidden_bits += (bin(pseudo[y])[2:][-1])
    
    hidden_bits = [hidden_bits[i:i+8] for i in range(0,len(hidden_bits),8)]

    for i in range(len(hidden_bits)):
        if message[-5:] == "$t3g0":
            break
        else :
            message += chr(int(hidden_bits[i],2))
    if(message[-5:] != "$t3g0"):
        message = ""

    if (len(message)!= 0):
        L2 = Label(frame,text = "Decode Successful \nMessage Found:")
        L2.config(font=("Magneto",11))
        L2.place(relx =0.8, rely =0.43 ,anchor= CENTER)
                 
        output = Label(frame,text = message[:-5])
        output.config(font=("Times New Roman",12),bd=10)
        output.place(relx=0.8,rely = 0.5 ,anchor = CENTER)
    else:
        L2 = Label(frame,text = "Decode Unsuccessful \n NO Message Found:")
        L2.config(font=("Magneto",11))
        L2.place(relx =0.8, rely =0.43 ,anchor= CENTER)
          
    
