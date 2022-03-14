from tkinter import *
from tkinter import ttk

root = Tk()
root.title("First_Program") #to give title
root.geometry('200x200')  #to set size of window

"""btn = Button(root,text= 'Click me!',bd='10',command=root.destroy)

btn.pack(side='top')      #pack(),grid(),place() used to implement the widget in window

user_name = Label(root, text = "Username").place(x = 40,y = 60)  
user_password = Label(root,text = "Password").place(x = 40,y = 100)  
submit_button = Button(root, text = "Submit").place(x = 40,y = 130)
user_name_input_area = Entry(root,width = 30).place(x = 110,y = 60)  
user_password_entry_area = Entry(root,width = 30).place(x = 110,y = 100)

w = Checkbutton ( root , option)
"""
C= Canvas(root,bg='green',height=300,width=300)

line = C.create_line(100,120,220,40,fill="blue")

#C.pack()


def paint( event ):
    
    # Co-ordinates.
    x1, y1, x2, y2 = ( event.x - 3 ),( event.y - 3 ), ( event.x + 3 ),( event.y + 3 )
     
    # Colour
    Colour = "#000fff000"
     
    # specify type of display
    w.create_line( x1, y1, x2,
                  y2, fill = Colour )
    print(event)
 
# create canvas widget.
w = Canvas(root, width = 400, height = 250)
 
# call function when double
# click is enabled.

w.bind( "<B1-Motion>", paint )
 
# create label.
l = Label( root, text = "Double Click and Drag to draw." )
l.pack()
w.pack()
root.mainloop()  #to run it

"""
anchor -> position control
bg -> background
height
width
bd -> border
font
cursor
textvariable
bitmap
fg
image
padx
pady
justify
relief
underline
wraplength
"""


"""
Canvas -> used to display various graphics on application

 .pack() -> used to implement the specific widget

widget.bind(event,handler)
    event-> defines what will tigger the handler eg enter,keypress etc
    handler->function that runs when tiggered
    

####motion of mouse For mouse wheel support under Linux, use Button-4 (scroll up)
    and Button-5 (scroll down) <B1-Motion> The mouse is moved, with mouse button 1
    being held down (use B2 for the middle button, B3 for the right button)

Combobox -> used to create a dropdown menu

StringVar(),  IntVar() are used to define the data type of Var used 

tkinter.Entry(parent,options) -> used to enter or display text

"""
