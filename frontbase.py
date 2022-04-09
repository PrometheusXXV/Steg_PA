#!/usr/bin/env python3


from time import strftime
from tkinter import ttk
from tkinter import filedialog
from tkinter.filedialog import *
import os
import PIL.Image
from PIL import ImageTk
from tkinter import *

from LSB import *  ########to import other files at module level make every thing as function but not as main otherwise main will run and cause problem
from PVD import *
from Audio_LSB import *
from custom_audio_enc import *
from phase_coding import *

#path = ''

def open_file(image_frame):
    file = filedialog.askopenfile(mode='r', filetypes =[('Files','*.png;*.jpg;*.jpeg')]) #'Files|*.jpg;*.jpeg;*.png;'
    global path
    if file:
        path = (os.path.abspath(file.name))          ### to get path using tkinter browse button
        file.close()
    print(path) 
    show_browse_file(path,image_frame)

def show_browse_file(path,image_frame): 
    x = Image.open(path)
    x = x.resize((250,250))
    img = ImageTk.PhotoImage(x)
    #img.resize((200,200))
   
    label =Label(image_frame, image=img)
    #previous_label =label
    #previous_label.destroy()
    label.place(anchor='e',relx =0.3,rely =0.6)
    label.image =img
    label.pack()

def clear_frame(frame):
      frame.destroy()

"""def menu_bar():
    
    menubar = Menu(root)
    #file menu
    file = Menu(menubar,tearoff=0)
    menubar.add_cascade(label="File" , menu=file)

    global current_frame
    file.add_command(label ='Home', command =None)
    file.add_separator()
    file.add_command(label ='Exit', command = root.destroy)

    #images steg menu
    images = Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Images" , menu=images)
    images.add_command(label ='LSB', command = lambda:[frame_main.destroy()])
    #images.add_command(label ='Masking and Filtering', command = None)
    images.add_command(label ='PVD', command = None)
    images.add_command(label ='PRNG', command = None)
    #images.add_command(label ='AES Encryption', command = None)

    #audio steg menu
    audio = Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Audio" , menu=audio)
    audio.add_command(label ='LSB', command = lambda:[current_frame.destroy(),LSB_Audio()])
    audio.add_command(label ='Custom', command = None)
    audio.add_command(label ='Phase Coding', command = None)
    #audio.add_command(label ='AES Encryption', command = None)

    root.config(menu=menubar)  #display menu
 """   

def win_LSB():
    root.title("STEG_PA - Image Steganography - LSB")
    frame_LSB = Frame(root)
    frame_LSB.pack(side="top", expand=True, fill="both")
    current_frame =frame_LSB
    path =''
    browse = Button(frame_LSB,text = "Browse",bd ='2', command = (lambda:[open_file(image_frame),label_used.destroy()])) ######### problem not able to store file path
    browse.config(font=("Courier",12))
    browse.place(relx=0.35,rely=0.1,anchor=CENTER)

    lsb_en = Button(frame_LSB,text = "Encode",bd ='2', command = (lambda:[None])) ######### problem not able to store file path
    lsb_en.config(font=("Courier",12))
    lsb_en.place(relx=0.5,rely=0.1,anchor=CENTER)

    lsb_de = Button(frame_LSB,text = "Decode",bd ='2', command = (lambda:[None])) ######### problem not able to store file path
    lsb_de.config(font=("Courier",12))
    lsb_de.place(relx=0.65,rely=0.1,anchor=CENTER)

    back = Button(frame_LSB,text = "BACK",bd='2',command=lambda:[frame_LSB.destroy(),Image_steg()])
    back.config(font=("Courier",16))
    back.place(relx=0.5,rely=0.8,anchor=CENTER)

    image_frame = Frame(frame_LSB, width=250, height=250,bg ='red')
    image_frame.pack()
    image_frame.place(anchor='center',relx=0.2,rely=0.40)
    #image_frame['padding'] = (5,10,5,10)

    x =PIL.Image.open(path)
    #x = x.resize((250,250))
    img = ImageTk.PhotoImage(x)
    #img.resize((200,200))
    label =Label(image_frame, image=img)
    
    label.place(anchor='e',relx =0.3,rely =0.6)
    label.image =img
    label.pack()
    
"""
def win_LSB():
    root.title("STEG_PA - Image Steganography - LSB")
    frame_LSB = Frame(root)
    frame_LSB.pack(side="top", expand=True, fill="both")
    
    lsb_en = Button(frame_LSB,text = "Encode",bd ='2', command = (lambda:[])) ######### problem not able to store file path
    lsb_en.config(font=("Courier",11))
    lsb_en.place(relx=0.5,rely=0.1,anchor=CENTER)

    lsb_de = Button(frame_LSB,text = "Decode",bd ='2', command = (lambda:[open_file()])) ######### problem not able to store file path
    lsb_de.config(font=("Courier",11))
    lsb_de.place(relx=0.5,rely=0.3,anchor=CENTER)

    back = Button(frame_LSB,text = "BACK",bd='2',command=lambda:[frame_LSB.destroy(),Image_steg()])
    back.config(font=("Courier",16))
    back.place(relx=0.5,rely=0.8,anchor=CENTER)
"""
def main_win():
    root.title("STEG_PA")
    global frame_main
    frame_main = Frame(root)
    current_frame =frame_main
    
    Images = Button(frame_main,text = "Image Steganography",bd='4',command=lambda:[frame_main.destroy(),Image_steg()])
    Images.config(font=("Courier",16))
    Images.place(relx=0.5,rely=0.3,anchor=CENTER)

    Audio = Button(frame_main,text = "Audio Steganography",bd='4',command=lambda:[frame_main.destroy(),Audio_steg()])
    Audio.config(font=("Courier",16))
    Audio.place(relx=0.5,rely=0.5,anchor=CENTER)
    
    Exit = Button(frame_main,text = "EXIT",bd='4',command=root.destroy)
    Exit.config(font=("Courier",16))
    Exit.place(relx=0.5,rely=0.7,anchor=CENTER)

    frame_main.pack(side="top", expand=True, fill="both")


def image_open(frame):
    global path
    file = filedialog.askopenfile(mode='r', filetypes =[('Files','*.png')]) #'Files|*.jpg;*.jpeg;*.png;'
    if file:
        path = (os.path.abspath(file.name))          ### to get path using tkinter browse button
        file.close()
    else :
        path =''
    print(path)
    if(len(path) != 0):
        path_output = Label(frame,text = "Image File Selected")
        path_output.config(font = ("magneto",13))
        path_output.place(relx = 0.2,rely = 0.12,anchor = CENTER)

        x = PIL.Image.open(path)
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
        label.place(anchor=CENTER,relx =0.2,rely =0.33)
        #label.pack()

        file = path.split('\\');
        file_name = Label(frame,text = file[-1])
        file_name.config(font = ("Times New Roman",13))
        file_name.place(relx = 0.2,rely = 0.55,anchor = CENTER)
        
    else:
        path_output = Label(frame,text = "Image File \nNot Selected")
        path_output.config(font = ("Magneto",13))
        path_output.place(relx = 0.2,rely = 0.12,anchor = CENTER)

        file_name = Label(frame,text ="                              ")
        file_name.config(font = ("Times New Roman",13))
        file_name.place(relx = 0.2,rely = 0.55,anchor = CENTER)

    
def image_pvd():
    root.title("STEG_PA - Image Steganography - PVD")

    frame_image_pvd = Frame(root)
    current_frame =frame_image_pvd

    browse = Button(frame_image_pvd,text = "Browse",command = lambda:[(image_open(frame_image_pvd))])
    browse.config(font = ("Courier",12))
    browse.place(relx = 0.35 ,rely = 0.7,anchor = CENTER)
    
    encode = Button(frame_image_pvd,text = "Encode",command = lambda:[pvd_encode(path,message_input,save_path,frame_image_pvd )])
    encode.config(font = ("Courier",12))
    encode.place(relx = 0.5 ,rely = 0.7,anchor = CENTER)
    
    decode = Button(frame_image_pvd,text = "Decode",command = lambda:[pvd_decode(path,frame_image_pvd)])
    decode.config(font = ("Courier",12))
    decode.place(relx = 0.65 ,rely = 0.7,anchor = CENTER)

    reset = Button(frame_image_pvd,text = "RESET",command = lambda:[clear_frame(frame_image_pvd),image_pvd()])
    reset.config(font = ("Courier",12))
    reset.place(relx = 0.5 ,rely = 0.8,anchor = CENTER)

    back =Button(frame_image_pvd,text = "Back", command =lambda:[frame_image_pvd.destroy(),Image_steg()])
    back.config(font = ("Courier",16))
    back.place(relx = 0.5 , rely =0.9, anchor = CENTER)

    message_input = Text(frame_image_pvd,height =4,width = 17)
    message_input.place(relx= 0.5,rely=0.17,anchor=CENTER)
    
    save_path =Text(frame_image_pvd,height =5,width =20)
    save_path.place(relx = 0.5 ,rely= 0.53, anchor =CENTER)

    L1 = Label(frame_image_pvd,text = "Enter Message \nTo encode")
    L1.config(font=("Magneto",11))
    L1.place(relx =0.5, rely =0.09 ,anchor= CENTER )

    L2 = Label(frame_image_pvd,text = "Enter File Name \nWith Extension to SAVE \nthe Encoded File")
    L2.config(font=("Magneto",11))
    L2.place(relx =0.5, rely =0.42 ,anchor= CENTER )

    frame_image_pvd.pack(side= "top",expand =True,fill = 'both')
    
        
def image_LSB():
    root.title("STEG_PA - Image Steganography - LSB")

    frame_image_lsb = Frame(root)
    current_frame =frame_image_lsb

    browse = Button(frame_image_lsb,text = "Browse",command = lambda:[(image_open(frame_image_lsb))])
    browse.config(font = ("Courier",12))
    browse.place(relx = 0.35 ,rely = 0.7,anchor = CENTER)
    
    encode = Button(frame_image_lsb,text = "Encode",command = lambda:[lsb_encode_image(path,message_input,save_path,frame_image_lsb )])
    encode.config(font = ("Courier",12))
    encode.place(relx = 0.5 ,rely = 0.7,anchor = CENTER)
    
    decode = Button(frame_image_lsb,text = "Decode",command = lambda:[lsb_decode_image(path,frame_image_lsb)])
    decode.config(font = ("Courier",12))
    decode.place(relx = 0.65 ,rely = 0.7,anchor = CENTER)

    reset = Button(frame_image_lsb,text = "RESET",command = lambda:[clear_frame(frame_image_lsb),image_LSB()])
    reset.config(font = ("Courier",12))
    reset.place(relx = 0.5 ,rely = 0.8,anchor = CENTER)

    back =Button(frame_image_lsb,text = "Back", command =lambda:[frame_image_lsb.destroy(),Image_steg()])
    back.config(font = ("Courier",16))
    back.place(relx = 0.5 , rely =0.9, anchor = CENTER)

    message_input = Text(frame_image_lsb,height =4,width = 17)
    message_input.place(relx= 0.5,rely=0.17,anchor=CENTER)
    
    save_path =Text(frame_image_lsb,height =5,width =20)
    save_path.place(relx = 0.5 ,rely= 0.53, anchor =CENTER)

    L1 = Label(frame_image_lsb,text = "Enter Message \nTo encode")
    L1.config(font=("Magneto",11))
    L1.place(relx =0.5, rely =0.09 ,anchor= CENTER )

    L2 = Label(frame_image_lsb,text = "Enter File Name \nWith Extension to SAVE \nthe Encoded File")
    L2.config(font=("Magneto",11))
    L2.place(relx =0.5, rely =0.42 ,anchor= CENTER )

    frame_image_lsb.pack(side= "top",expand =True,fill = 'both')
    
def Image_steg():
    root.title("STEG_PA - Image Steganography")
       
    frame_image= Frame(root)
    current_frame =frame_image
    LSB = Button(frame_image,text = "LSB",bd='4',command=lambda:[frame_image.destroy(),image_LSB()])
    LSB.config(font=("Courier",16))
    LSB.place(relx=0.5,rely=0.2,anchor=CENTER)

    """mask = Button(frame_image,text = "MASKING AND FILTERING",bd='4',command=None)
    mask.config(font=("Courier",16))
    mask.place(relx=0.5,rely=0.65,anchor=CENTER)
    """
    PVD = Button(frame_image,text = "PVD",bd='4',command=None)
    PVD.config(font=("Courier",16))
    PVD.place(relx=0.5,rely=0.35,anchor=CENTER)

    PRNG = Button(frame_image,text = "PRNG",bd='4',command=None)
    PRNG.config(font=("Courier",16))
    PRNG.place(relx=0.5,rely=0.5,anchor=CENTER)

    back = Button(frame_image,text = "BACK",bd='4',command=lambda:[frame_image.destroy(),main_win()])
    back.config(font=("Courier",16))
    back.place(relx=0.5,rely=0.9,anchor=CENTER)
    
    frame_image.pack(side="top", expand=True, fill="both")

    

    

def audio_open(frame):
    global path
    file = filedialog.askopenfile(mode='r', filetypes =[('Files','*.wav')]) #'Files|*.jpg;*.jpeg;*.png;'
    if file:
        path = (os.path.abspath(file.name))          ### to get path using tkinter browse button
        file.close()
    else :
        path =''
    print(path)
    if(len(path) != 0):
        ########dekhna hai abhi ise #######Label(frame,text = "                              ").place(relx=0.2,rely =0.2,anchor=CENTER)
        path_output = Label(frame,text = "Audio File Selected")
        path_output.config(font = ("magneto",13))
        path_output.place(relx = 0.2,rely = 0.25,anchor = CENTER)

        file = path.split('\\');
        file_name = Label(frame,text = file[-1])
        file_name.config(font = ("Times New Roman",13))
        file_name.place(relx = 0.2,rely = 0.35,anchor = CENTER)

    else:
        path_output = Label(frame,text = "Audio File \nNot Selected")
        path_output.config(font = ("Magneto",13))
        path_output.place(relx = 0.2,rely = 0.25,anchor = CENTER)

        file_name = Label(frame,text ="                              ")
        file_name.config(font = ("Times New Roman",13))
        file_name.place(relx = 0.2,rely = 0.35,anchor = CENTER)

def LSB_Audio():
    root.title("STEG_PA - Audio Steganography - LSB")

    frame_audio_lsb = Frame(root)
    current_frame =frame_audio_lsb

    browse = Button(frame_audio_lsb,text = "Browse",command = lambda:[(audio_open(frame_audio_lsb))])
    browse.config(font = ("Courier",12))
    browse.place(relx = 0.35 ,rely = 0.7,anchor = CENTER)
    
    encode = Button(frame_audio_lsb,text = "Encode",command = lambda:[a_lsb_encode(path,message_input,save_path,frame_audio_lsb )])
    encode.config(font = ("Courier",12))
    encode.place(relx = 0.5 ,rely = 0.7,anchor = CENTER)
    
    decode = Button(frame_audio_lsb,text = "Decode",command = lambda:[a_lsb_decode(path,frame_audio_lsb)])
    decode.config(font = ("Courier",12))
    decode.place(relx = 0.65 ,rely = 0.7,anchor = CENTER)

    reset = Button(frame_audio_lsb,text = "RESET",command = lambda:[clear_frame(frame_audio_lsb),LSB_Audio()])
    reset.config(font = ("Courier",12))
    reset.place(relx = 0.5 ,rely = 0.8,anchor = CENTER)

    back =Button(frame_audio_lsb,text = "Back", command =lambda:[frame_audio_lsb.destroy(),Audio_steg()])
    back.config(font = ("Courier",16))
    back.place(relx = 0.5 , rely =0.9, anchor = CENTER)


    message_input = Text(frame_audio_lsb,height =10,width = 17)
    message_input.place(relx= 0.5,rely=0.3,anchor=CENTER)
    
    save_path =Text(frame_audio_lsb,height =5,width =30)
    save_path.place(relx = 0.8 ,rely= 0.24, anchor =CENTER)

    L1 = Label(frame_audio_lsb,text = "Enter Message \nTo encode")
    L1.config(font=("Magneto",11))
    L1.place(relx =0.5, rely =0.15 ,anchor= CENTER )

    L2 = Label(frame_audio_lsb,text = "Enter File Name \nWith Extension to SAVE \nthe Encoded File")
    L2.config(font=("Magneto",11))
    L2.place(relx =0.8, rely =0.13 ,anchor= CENTER )

    frame_audio_lsb.pack(side= "top",expand =True,fill = 'both')



def custom_audio():
    root.title("STEG_PA - Audio Steganography - CUSTOM")

    frame_audio_custom = Frame(root)
    current_frame =frame_audio_custom

    browse = Button(frame_audio_custom,text = "Browse",command = lambda:[(audio_open(frame_audio_custom))])
    browse.config(font = ("Courier",12))
    browse.place(relx = 0.35 ,rely = 0.7,anchor = CENTER)
    
    encode = Button(frame_audio_custom,text = "Encode",command = lambda:[custom_encode(message_input,frame_audio_custom,seed_input,save_path,path)])
    encode.config(font = ("Courier",12))
    encode.place(relx = 0.5 ,rely = 0.7,anchor = CENTER)
    
    decode = Button(frame_audio_custom,text = "Decode",command = lambda:[custom_decode(frame_audio_custom,seed_input,path)])
    decode.config(font = ("Courier",12))
    decode.place(relx = 0.65 ,rely = 0.7,anchor = CENTER)

    reset = Button(frame_audio_custom,text = "RESET",command = lambda:[clear_frame(frame_audio_custom),custom_audio()])
    reset.config(font = ("Courier",12))
    reset.place(relx = 0.5 ,rely = 0.8,anchor = CENTER)

    back =Button(frame_audio_custom,text = "Back", command =lambda:[frame_audio_custom.destroy(),Audio_steg()])
    back.config(font = ("Courier",16))
    back.place(relx = 0.5 , rely =0.9, anchor = CENTER)

    message_input = Text(frame_audio_custom,height =4,width = 17)
    message_input.place(relx= 0.5,rely=0.2,anchor=CENTER)

    seed_input = Text(frame_audio_custom,height =4,width = 17)
    seed_input.place(relx = 0.5 ,rely=0.47,anchor = CENTER)

    save_path =Text(frame_audio_custom,height =5,width =25)
    save_path.place(relx = 0.8 ,rely= 0.24, anchor =CENTER)

    L1 = Label(frame_audio_custom,text = "Enter Message \nTo encode")
    L1.config(font=("Magneto",11))
    L1.place(relx =0.5, rely =0.12 ,anchor= CENTER )

    L1 = Label(frame_audio_custom,text = "Enter the Seed")
    L1.config(font=("Magneto",11))
    L1.place(relx =0.5, rely =0.40 ,anchor= CENTER )

    L1 = Label(frame_audio_custom,text = "Enter File Name \nWith Extension to SAVE \nthe Encoded File")
    L1.config(font=("Magneto",11))
    L1.place(relx =0.8, rely =0.13 ,anchor= CENTER) 

    frame_audio_custom.pack(side = 'top',expand = True, fill = 'both')
    
def phase_coding_audio():
    root.title("STEG_PA - Audio Steganography - PHASE CODING")

    frame_audio_pc = Frame(root)
    current_frame =frame_audio_pc

    browse = Button(frame_audio_pc,text = "Browse",command = lambda:[(audio_open(frame_audio_pc))])
    browse.config(font = ("Courier",12))
    browse.place(relx = 0.35 ,rely = 0.7,anchor = CENTER)
    
    encode = Button(frame_audio_pc,text = "Encode",command = lambda:[phase_encode(message_input,frame_audio_pc,save_path,path)])
    encode.config(font = ("Courier",12))
    encode.place(relx = 0.5 ,rely = 0.7,anchor = CENTER)
    
    decode = Button(frame_audio_pc,text = "Decode",command = lambda:[phase_decode(frame_audio_pc,path)])
    decode.config(font = ("Courier",12))
    decode.place(relx = 0.65 ,rely = 0.7,anchor = CENTER)

    reset = Button(frame_audio_pc,text = "RESET",command = lambda:[clear_frame(frame_audio_pc),phase_coding_audio()])
    reset.config(font = ("Courier",12))
    reset.place(relx = 0.5 ,rely = 0.8,anchor = CENTER)

    back =Button(frame_audio_pc,text = "Back", command =lambda:[frame_audio_pc.destroy(),Audio_steg()])
    back.config(font = ("Courier",16))
    back.place(relx = 0.5 , rely =0.9, anchor = CENTER)

    message_input = Text(frame_audio_pc,height =4,width = 17)
    message_input.place(relx= 0.5,rely=0.2,anchor=CENTER)

    save_path =Text(frame_audio_pc,height =5,width =25)
    save_path.place(relx = 0.8 ,rely= 0.24, anchor =CENTER)

    L1 = Label(frame_audio_pc,text = "Enter Message \nTo encode")
    L1.config(font=("Magneto",11))
    L1.place(relx =0.5, rely =0.12 ,anchor= CENTER )

    L1 = Label(frame_audio_pc,text = "Enter File Name \nWith Extension to SAVE \nthe Encoded File")
    L1.config(font=("Magneto",11))
    L1.place(relx =0.8, rely =0.13 ,anchor= CENTER) 


    frame_audio_pc.pack(side='top', expand = True, fill = 'both')
    

def Audio_steg():######## root change karna hai
    root.title("STEG_PA - Audio Steganography")
       
    frame_audio= Frame(root)
    current_frame =frame_audio
    
    LSB = Button(root,text = "LSB",bd='4',command=lambda:[frame_audio.destroy(),LSB_Audio()])
    LSB.config(font=("Courier",16))
    LSB.place(relx=0.5,rely=0.2,anchor=CENTER)

    CUS = Button(root,text = "CUSTOM",bd='4',command=lambda:[frame_audio.destroy(),custom_audio()])
    CUS.config(font=("Courier",16))
    CUS.place(relx=0.5,rely=0.35,anchor=CENTER)

    PC = Button(root,text = "PHASE CODING",bd='4',command=lambda:[frame_audio.destroy(),phase_coding_audio()])
    PC.config(font=("Courier",16))
    PC.place(relx=0.5,rely=0.5,anchor=CENTER)


    back = Button(root,text = "BACK",bd='4',command=lambda:[frame_audio.destroy(),main_win()])
    back.config(font=("Courier",16))
    back.place(relx=0.5,rely=0.9,anchor=CENTER)

    frame_audio.pack(side="top", expand=True, fill="both")
    

    
root =Tk()
root.geometry("800x700")
#menu_bar()
#LSB_Audio()
#main_win()
#Image_steg()
#Audio_steg()
#phase_coding_audio()
#image_LSB()
image_pvd()
#win_LSB()
#custom_audio()
root.mainloop()

#  from LSB import *  ########to import other files at module level make every thing as function but not as main otherwise main will run and cause problem
