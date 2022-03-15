from tkinter import *
from time import strftime

root =Tk()
root.geometry("800x600")
root.title("STEG_PA")

menubar = Menu(root)
#file menu
file = Menu(menubar,tearoff=0)
menubar.add_cascade(label="File" , menu=file)

file.add_command(label ='New File', command = None)
file.add_command(label ='Open...', command = None)
file.add_command(label ='Save', command = None)
file.add_separator()
file.add_command(label ='Exit', command = root.destroy)

#audio steg menu
audio = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Audio" , menu=audio)
audio.add_command(label ='LSB', command = None)
audio.add_command(label ='Spread Spectrum', command = None)
audio.add_command(label ='Echo Hiding', command = None)
audio.add_command(label ='AES', command = None)
audio.add_command(label ='Tone Insertion', command = None)
audio.add_command(label ='Phase Coding', command = None)

#images steg menu
images = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Images" , menu=images)
images.add_command(label ='Whitespace', command = None)
images.add_command(label ='Masking and Filtering', command = None)
images.add_command(label ='Distotion Technique', command = None)
images.add_command(label ='AES', command = None)
images.add_command(label ='PVD', command = None)
images.add_command(label ='PRNG', command = None)

root.config(menu=menubar)  #display menu

root.mainloop()