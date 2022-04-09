import PIL.Image
from PIL import ImageTk
from tkinter import *
from math import floor,ceil

def message_to_bits(data):          ### for encoding
    newdata = []
    newdata.append([format(ord(i), "08b") for i in data])
    return newdata[0]

def new_value(prev_1,prev_2,dr,db,dg):
    new_1=[0,0,0]
    new_2=[0,0,0]
    val_r = int(dr,2)
    change_r_1 = floor(val_r/2)
    change_r_2 = ceil(val_r/2)
    new_1[0] =int(format(prev_1[0],"08b")[0:5]+format(change_r_1,"08b")[-3:],2)
    new_2[0] =int(format(prev_2[0],"08b")[0:5]+format(change_r_2,"08b")[-3:],2)
    
    val_g = int(dg,2)
    change_g_1 = floor(val_g/2)
    change_g_2 = ceil(val_g/2)
    new_1[1] = int(format(prev_1[1],"08b")[0:5]+(format(change_g_1,"08b")[-3:]),2)
    new_2[1] = int(format(prev_2[1],"08b")[0:5]+(format(change_g_2,"08b")[-3:]),2)

    val_b = int(db,2)
    change_b_1 = floor(val_b/2)
    change_b_2 = ceil(val_b/2)
    new_1[2] = int(format(prev_1[2],"08b")[0:6]+(format(change_b_1,"08b")[-2:]),2)
    new_2[2] = int(format(prev_2[2],"08b")[0:6]+(format(change_b_2,"08b")[-2:]),2)
    
    return tuple(new_1),tuple(new_2)

def pvd_encode(img_path,message_input,save_path,frame):
    message = message_input.get(1.0,"end-1c")
    path_to_save_file = save_path.get(1.0,"end-1c")

    if(len(img_path)==0):
        L4 = Label(frame,text = "No Audio File Selected")
        L4.config(font = ("Times New Roman",12))
        L4.place(relx = 0.2,rely =0.5,anchor =CENTER)
    elif(len(message) == 0):
        L4 = Label(frame,text = "No Message Entered \n Enter the Message to Hide")
        L4.config(font = ("Times New Roman",12))
        L4.place(relx = 0.5,rely =0.5,anchor =CENTER)
    elif(len(path_to_save_file)==0):
        L5 = Label(frame,text = "Enter the file name \nto save the encoded file \nto procedd")
        L5.config(font = ("Times New Roman",12))
        L5.place(relx=0.8,rely=0.35,anchor=CENTER)
    else:
        message = message + "$t3g0"
        cover = PIL.Image.open(img_path)
        cover = cover.convert("RGB")
        
        data = message_to_bits(message)
        len_data = len(data)

        wd, ht = cover.size
        pixel =list(cover.getdata())
        total_pixel=len(pixel)

        for i in range(len_data):
            a = pixel[2*i]
            b = pixel[2*i+1]

            ###### R mein 3
            ###### G mein 2
            ###### B mein 3

            pseudo =data[i]
            dr = pseudo[0:3]
            dg = pseudo[3:6]
            db = pseudo[6:]
            a_new,b_new = new_value(a,b,dr,db,dg)
            
            pixel[2*i] = a_new
            pixel[(2*i)+1] = b_new
        
        for x in range(wd):
            for y in range(ht):
                cover.putpixel((x,y),pixel[(y*wd+x)])
        cover.save(path_to_save_file,str(path_to_save_file.split('.')[1].upper()))
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

def pvd_decode(img_path,frame):
    cover = PIL.Image.open(img_path)
    
    pixel = list(cover.getdata())
    total_pixel =len(pixel)
    counter = 0 
    message =''
    while(message[-5:]!="$t3g0"):
        
        a= pixel[2*counter]
        b= pixel[2*counter+1]
        mess =''
        for j in range(3):
            if(j==0 or j==1):
                x = int(format(a[j],"08b")[-3:],2)
                y = int(format(b[j],"08b")[-3:],2)
                req =x+y
                mess += format(req,"08b")[-3:]
            else:
                x = int(format(a[j],"08b")[-2:],2)
                y = int(format(b[j],"08b")[-2:],2)
                req =x+y
                mess += format(req,"08b")[-2:]

        message += chr(int(mess,2))
        counter += 1

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
        
#print(message_to_bits("ABHINAV"))
"""cover = Image.open("D:\IIT_DHANBAD\CYBERLABS\STEG_PA\message.png")
message=input("Enter the message : ")
message = message+"$t3g0"
cover.convert("RGB")
cover_2 = pvd_encode(cover,message)
cover_2.save("D:\IIT_DHANBAD\CYBERLABS\STEG_PA\pvd_encoded.png")


xyz = Image.open("D:\IIT_DHANBAD\CYBERLABS\STEG_PA\pvd_encoded.png")
pvd_decode(xyz)


"""
