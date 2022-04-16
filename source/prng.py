import PIL.Image
from PIL import ImageTk
from tkinter import *

def message_to_bits(data):          ### for encoding
    newdata = []
    newdata.append([format(ord(i), "08b") for i in data])
    return newdata[0]

def gcd(p,q):
    while q!=0:
        p,q = q , p%q
    return p


def prng_calc(len_message,seed,inc):
    for i in range (len_message,len_message+50):
        if(i>inc):
            if(gcd(i,inc)==1):
                mod =i
                #print(mod)
                break

    return mod
    
def prng_pixel(s,inc,m,len_message):
    pix = []
    for i in range(len_message):
        req = (s+inc)%m
        pix.append(req)
        s =pix[i]

    return pix
    

def prng_encode_image(path,message_input,save_path,seed_input,increment_input,frame):
    message = message_input.get(1.0,"end-1c")
    path_to_save_file = save_path.get(1.0,"end-1c")
    seed = seed_input.get(1.0,"end-1c")
    increment = increment_input.get(1.0,"end-1c")

    if(len(path)==0):
        L4 = Label(frame,text = "No Image Selected")
        L4.config(font = ("Times New Roman",12))
        L4.place(relx = 0.2,rely =0.5,anchor =CENTER)
    elif(len(message) == 0):
        L4 = Label(frame,text = "No Message Entered \n Enter the Message to Hide")
        L4.config(font = ("Times New Roman",12))
        L4.place(relx = 0.5,rely =0.23,anchor =CENTER)
    elif(len(path_to_save_file)==0):
        L5 = Label(frame,text = "Enter the file name \nto save the encoded file \nto procedd")
        L5.config(font = ("Times New Roman",12))
        L5.place(relx=0.8,rely=0.64,anchor=CENTER)
    
    elif(len(seed)==0):
        L4 = Label(frame,text = "Enter the\nSeed")
        L4.config(font = ("Times New Roman",12))
        L4.place(relx = 0.43,rely =0.42,anchor =CENTER)  
    elif(len(increment)==0):
        L4 = Label(frame,text = "Enter the\nIncrement")
        L4.config(font = ("Times New Roman",12))
        L4.place(relx = 0.57,rely =0.42,anchor =CENTER)

    else:
        seed = int(seed)
        increment = int(increment)
        cover = PIL.Image.open(path,'r')
        cover = cover.convert("RGB")
        wd,ht = cover.size
        message = message+"$t3g0"
        
        mess_in_bits = message_to_bits(message)

        mod = prng_calc(len(message),seed,increment)
        req_pixel = prng_pixel(seed,increment,mod,len(message))
        #print(req_pixel)

        img_pixel= list(cover.getdata())

        for i in range(len(req_pixel)):
            new_pseudo =[0,0,0]
            pseudo = img_pixel[req_pixel[i]]
            data = ord(message[i])
            #print(req_pixel[i],pseudo)
            new_pseudo[0] = int((format(pseudo[0],"08b")[0:5]+format(data,"08b")[:3]),2)
            new_pseudo[1] = int((format(pseudo[1],"08b")[0:6]+format(data,"08b")[3:5]),2)
            new_pseudo[2] = int((format(pseudo[2],"08b")[0:5]+format(data,"08b")[5:]),2)

            #print(pseudo,format(data,"08b"),new_pseudo)
            img_pixel[req_pixel[i]] = tuple(new_pseudo)

        for x in range(wd):
            for y in range(ht):
                cover.putpixel((x,y),img_pixel[(y*wd+x)])

        cover.save(path_to_save_file)

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

    
def prng_decode_image(path,seed_input,increment_input,frame):
#def prng_decode():
    seed = seed_input.get(1.0,"end-1c")
    increment = increment_input.get(1.0,"end-1c")
    seed =int(seed)
    increment =int(increment)
    cover = PIL.Image.open("save_prng_222.png",'r')
    cover = cover.convert("RGB")
    wd,ht = cover.size
    img_pixel= list(cover.getdata())
    i=0
    message=''
    while(message[-5:]!="$t3g0" and (i<len(img_pixel) or i<200)):
    #for i in range(1,15):
        message =''
        len_message=i;
        mod = prng_calc(len_message,seed,increment)
        req_pixel = prng_pixel(seed,increment,mod,len_message)
        
        for j in range(len(req_pixel)):
            mess = ''
            pseudo = img_pixel[req_pixel[j]]
            mess += format(pseudo[0],"08b")[-3:]
            mess += format(pseudo[1],"08b")[-2:]
            mess += format(pseudo[2],"08b")[-3:]
            message += chr(int(mess,2))

        print(message)

        i+=1

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

    
#prng_calc(14,2,12)
#prng_pixel(2,3,16,17)
#prng_encode()
#prng_decode()


