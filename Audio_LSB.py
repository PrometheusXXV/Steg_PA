import wave
from tkinter import *
def message_to_bits(data):          ### for encoding
    newdata =[]
    newdata= ''.join([format(ord(i), "08b") for i in data])
    return newdata

def a_lsb_encode(path,mess_input,save_path,frame):#mess_input,frame,save_path
    message = mess_input.get(1.0,"end-1c")
    path_to_save_file = save_path.get(1.0,"end-1c")
    
    if(len(path)==0):
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
        song = wave.open(path,mode = 'r')
        song_frames = list(song.readframes(song.getnframes()))
        message = message + "$t0p"              ### added to stop the read of code when decrypting
        mess = message_to_bits(message)
        #print(mess)
        #print(song_frames[0:100])
        new_song_frames=[]
        for i in range(len(song_frames)):
            if ( i<len(mess)):
                frame_byte = bin(song_frames[i])
                frame_byte_modified = frame_byte[2:9]+mess[i]
                #print(frame_byte_modified)
                new_song_frames.append(int(frame_byte_modified,2))
            else:
                new_song_frames.append(song_frames[i])

        #print(new_song_frames[0:100])
        frame_modified_final = bytes(new_song_frames)
        with wave.open(path_to_save_file,'w') as final:
            final.setparams(song.getparams())
            final.writeframes(frame_modified_final)

        song.close()
        enc_mess = Label(frame,text = "Message Successfully \nEncoded")
        enc_mess.config(font = ("Times New Romar",11))
        enc_mess.place(relx = 0.8,rely = 0.35,anchor = CENTER)
        
def dec_8b(enc_8b):
    x = int(enc_8b,2)
    return chr(x)

def a_lsb_decode(path,frame):
    enc_message =''
    song = wave.open(path,mode = 'r')
    song_frames = list(song.readframes(song.getnframes()))
    mess = ''
    for i in range(len(song_frames)):
        if(enc_message[-4:] != "$t0p"):
            frame_bytes = bin(song_frames[i])
            mess =mess + frame_bytes[-1]
            if(len(mess)==8):
                enc_message = enc_message + dec_8b(mess)
                mess =''

    if(enc_message[-4:]!="$t0p"):
        enc_message = ''
        
    if (len(enc_message)!= 0):
        L2 = Label(frame,text = "Decode Successful \nMessage Found:")
        L2.config(font=("Magneto",11))
        L2.place(relx =0.8, rely =0.43 ,anchor= CENTER)
                 
        output = Label(frame,text = enc_message[:-4])
        output.config(font=("Times New Roman",12),bd=10)
        output.place(relx=0.8,rely = 0.5 ,anchor = CENTER)
    else:
        L2 = Label(frame,text = "Decode Unsuccessful \n NO Message Found:")
        L2.config(font=("Magneto",11))
        L2.place(relx =0.8, rely =0.43 ,anchor= CENTER)
