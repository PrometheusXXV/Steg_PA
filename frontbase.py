from tkinter import *
from time import strftime


def menu_bar():
    
    menubar = Menu(root)
    #file menu
    file = Menu(menubar,tearoff=0)
    menubar.add_cascade(label="File" , menu=file)

    file.add_command(label ='New File', command = None)
    file.add_command(label ='Open...', command = None)
    file.add_command(label ='Save', command = None)
    file.add_separator()
    file.add_command(label ='Exit', command = root.destroy)

    #images steg menu
    images = Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Images" , menu=images)
    images.add_command(label ='LSB', command = None)
    images.add_command(label ='Whitespace', command = None)
    images.add_command(label ='Masking and Filtering', command = None)
    images.add_command(label ='Distotion Technique', command = None)
    images.add_command(label ='PVD', command = None)
    images.add_command(label ='PRNG', command = None)
    #images.add_command(label ='AES Encryption', command = None)

    #audio steg menu
    audio = Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Audio" , menu=audio)
    audio.add_command(label ='LSB', command = None)
    audio.add_command(label ='Spread Spectrum', command = None)
    audio.add_command(label ='Echo Hiding', command = None)
    audio.add_command(label ='Tone Insertion', command = None)
    audio.add_command(label ='Phase Coding', command = None)
    #audio.add_command(label ='AES Encryption', command = None)

    root.config(menu=menubar)  #display menu
    

def main_win():
    root.title("STEG_PA")
    frame_main = Frame(root)
    
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
    
def Image_steg():
    root.title("STEG_PA - Image Steganography")
       
    frame_image= Frame(root)    
    LSB = Button(frame_image,text = "LSB",bd='4',command=None)
    LSB.config(font=("Courier",16))
    LSB.place(relx=0.5,rely=0.2,anchor=CENTER)

    Whitespace = Button(frame_image,text = "WHITESPACE STEGANOGRAPHY",bd='4',command=None)
    Whitespace.config(font=("Courier",16))
    Whitespace.place(relx=0.5,rely=0.3,anchor=CENTER)

    mask = Button(frame_image,text = "MASKING AND FILTERING",bd='4',command=None)
    mask.config(font=("Courier",16))
    mask.place(relx=0.5,rely=0.4,anchor=CENTER)

    dis = Button(frame_image,text = "DISTORTION TECHNIQUE",bd='4',command=None)
    dis.config(font=("Courier",16))
    dis.place(relx=0.5,rely=0.5,anchor=CENTER)

    PVD = Button(frame_image,text = "PVD",bd='4',command=None)
    PVD.config(font=("Courier",16))
    PVD.place(relx=0.5,rely=0.6,anchor=CENTER)

    PRNG = Button(frame_image,text = "PRNG",bd='4',command=None)
    PRNG.config(font=("Courier",16))
    PRNG.place(relx=0.5,rely=0.7,anchor=CENTER)

    back = Button(frame_image,text = "BACK",bd='4',command=lambda:[frame_image.destroy(),main_win()])
    back.config(font=("Courier",16))
    back.place(relx=0.5,rely=0.8,anchor=CENTER)

    frame_image.pack(side="top", expand=True, fill="both")



def Audio_steg():
    root.title("STEG_PA - Audio Steganography")
       
    frame_audio= Frame(root)    
    
    LSB = Button(root,text = "LSB",bd='4',command=None)
    LSB.config(font=("Courier",16))
    LSB.place(relx=0.5,rely=0.2,anchor=CENTER)

    echo = Button(root,text = "ECHO HIDING",bd='4',command=None)
    echo.config(font=("Courier",16))
    echo.place(relx=0.5,rely=0.3,anchor=CENTER)

    SS = Button(root,text = "SPREAD SPECTRUM",bd='4',command=None)
    SS.config(font=("Courier",16))
    SS.place(relx=0.5,rely=0.4,anchor=CENTER)

    PC = Button(root,text = "PHASE CODING",bd='4',command=None)
    PC.config(font=("Courier",16))
    PC.place(relx=0.5,rely=0.5,anchor=CENTER)

    TI = Button(root,text = "TONE INSTERTION",bd='4',command=None)
    TI.config(font=("Courier",16))
    TI.place(relx=0.5,rely=0.6,anchor=CENTER)

    back = Button(root,text = "BACK",bd='4',command=lambda:[frame_audio.destroy(),main_win()])
    back.config(font=("Courier",16))
    back.place(relx=0.5,rely=0.8,anchor=CENTER)

    frame_audio.pack(side="top", expand=True, fill="both")
    
root =Tk()
root.geometry("800x600")
menu_bar()
main_win()
#Image_steg()
#Audio_steg()
root.mainloop()

