import PIL.Image
from PIL import ImageTk
from tkinter import *

def pixel_to_bits(img):
    pixel = list(img.getdata())
    for i in range(len(pixel)):
        pseudo = list(pixel[i])
        for j in range(3):
            temp = pseudo[j]
            pseudo[j] = format(temp,"08b")
        pixel[i] = tuple(pseudo)

    return pixel

def bits_to_pixel(pixel):
    for i in range(len(pixel)):
        pseudo = list(pixel[i])
        for j in range(3):
            temp = pseudo[j]
            pseudo[j] = int(temp,2)
        pixel[i] = tuple(pseudo)

    return(pixel)
    
def merge(img,img_2):
    pixel_bits=[]
    wd,ht = img.size
    pixel_list_1 = pixel_to_bits(img)
    pixel_list_2 = pixel_to_bits(img_2)
    for i in range(len(pixel_list_1)):
        pseudo_1 = pixel_list_1[i]
        pseudo_2 = pixel_list_2[i]
        new_pixel = [0,0,0]
        for j in range(3):
            temp_1= pseudo_1[j]
            temp_2= pseudo_2[j]
            new_pixel[j] = temp_1[0:4]+temp_2[0:4]

        pixel_bits.append(tuple(new_pixel))
    pixel = bits_to_pixel(pixel_bits)
    
    pseudo_img = PIL.Image.new("RGB",size=(wd,ht))
    for x in range(wd):
        for y in range(ht):
            pseudo_img.putpixel((x,y),pixel[(y*wd+x)])

    return pseudo_img
    
def ih_encode(img_path,cover_path,save_path,frame):
    path_to_save_file = save_path.get(1.0,"end-1c")
    
    if(len(img_path)==0):
        L4 = Label(frame,text = "No Audio File Selected")
        L4.config(font = ("Times New Roman",12))
        L4.place(relx = 0.2,rely =0.5,anchor =CENTER)
    elif(len(cover_path) == 0):
        L4 = Label(frame,text = "No Message Entered \n Enter the Message to Hide")
        L4.config(font = ("Times New Roman",12))
        L4.place(relx = 0.5,rely =0.5,anchor =CENTER)
    elif(len(path_to_save_file)==0):
        L5 = Label(frame,text = "Enter the file name \nto save the encoded file \nto procedd")
        L5.config(font = ("Times New Roman",12))
        L5.place(relx=0.8,rely=0.35,anchor=CENTER)
    else:
        img = PIL.Image.open(cover_path,'r')
        img = img.convert("RGB")
        img_2 = PIL.Image.open(img_path,'r')
        img_2 = img_2.convert("RGB")
        wd,ht = img.size
        
        img_2 = img_2.resize((wd,ht))
        merged_image = merge(img,img_2)

        merged_image.save(path_to_save_file,str(path_to_save_file.split('.')[1].upper()))
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
    
def split(img):
    pixel_bits = pixel_to_bits(img)
    wd,ht = img.size
    pixel_1 = []
    pixel_2 = []
    for i in range(len(pixel_bits)):
        pseudo = pixel_bits[i]
        new_pixel_1 = [0,0,0]
        new_pixel_2 = [0,0,0]
        for j in range(3):
            temp = pseudo[j]
            new_pixel_1[j] = temp[0:4]+'0000'
            new_pixel_2[j] = temp[4:8]+'0000'

        pixel_1.append(tuple(new_pixel_1))
        pixel_2.append(tuple(new_pixel_2))

    pixel = bits_to_pixel(pixel_1)
    pseudo_img = PIL.Image.new("RGB",size=(wd,ht))
    for x in range(wd):
        for y in range(ht):
            pseudo_img.putpixel((x,y),pixel[(y*wd+x)])

    pixel = bits_to_pixel(pixel_2)
    pseudo_img_2 = PIL.Image.new("RGB",size=(wd,ht))
    for x in range(wd):
        for y in range(ht):
            pseudo_img_2.putpixel((x,y),pixel[(y*wd+x)])

    return pseudo_img , pseudo_img_2
    
def ih_decode(cover_path,frame):
    
    img = PIL.Image.open(cover_path,'r')
    img = img.convert("RGB")
    cover_img ,hidden_img = split(img)

    L2 = Label(frame,text = "Decode Successful \n\nHidden Image:")
    L2.config(font=("Magneto",11))
    L2.place(relx =0.85, rely =0.13 ,anchor= CENTER)

    wd,ht = hidden_img.size
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

    hidden_img = hidden_img.resize((wd,ht))
    img = ImageTk.PhotoImage(hidden_img)
    label =Label(frame, image=img)
    label.image =img
    label.place(anchor=CENTER,relx =0.85,rely =0.33)


    L2 = Label(frame,text = "Orginal Cover Image:")
    L2.config(font=("Magneto",11))
    L2.place(relx =0.15, rely =0.13 ,anchor= CENTER)

    wd,ht = hidden_img.size
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

    cover_img = cover_img.resize((wd,ht))
    img = ImageTk.PhotoImage(cover_img)
    label =Label(frame, image=img)
    label.image =img
    label.place(anchor=CENTER,relx =0.15,rely =0.33)
    
