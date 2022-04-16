import os.path

import numpy as np
from scipy.io import wavfile
from tkinter import *


def phase_encode(message_input,frame,save_path,path_to_file):
    message = message_input.get(1.0,'end-1c')
    if(len(message)!=0):
        message =message+'$t3g0'
    path_to_save_file = save_path.get(1.0,'end-1c')
    if(len(path_to_file)==0):
        L4 = Label(frame,text = "No Audio File Selected")
        L4.config(font = ("Times New Roman",12))
        L4.place(relx = 0.2,rely =0.5,anchor =CENTER)
    elif(len(message) == 0):
        L4 = Label(frame,text = "No Message Entered \n Enter the Message to Hide")
        L4.config(font = ("Times New Roman",12))
        L4.place(relx = 0.5,rely =0.3,anchor =CENTER)
    elif(len(path_to_save_file)==0):
        L5 = Label(frame,text = "Enter the file name \nto save the encoded file \nto procedd")
        L5.config(font = ("Times New Roman",12))
        L5.place(relx=0.8,rely=0.35,anchor=CENTER)
    else:        

        rate, data_1 = wavfile.read(path_to_file)
        message = message.ljust(150,'`')            #### can store message of 150 bytes for easier decoding
        mess_len = 8*len(message)
        chunksize = int(2*2**np.ceil(np.log2(2*mess_len)))
        number_of_chunks = int(np.ceil(data_1.shape[0]/chunksize))
        
        data = data_1.copy()            ### created a copy if further comparision needed

        if(len(data_1.shape)==1):
            data.resize(number_of_chunks*chunksize)
            data = data[np.newaxis]
            print(data.shape)

        else:
            data.resize((number_of_chunks*chunksize,data.shape[1]))
            data =data.T     #### transpose the array
            #print(data.shape)

        chunks = data[0].reshape((number_of_chunks, chunksize))

        chunks = np.fft.fft(chunks)         ### Fast fourier Transformation
        magnitudes =np.abs(chunks)
        phases =np.angle(chunks)
        phasediff = np.diff(phases,axis=0 )

        
        mess = np.ravel([[int(y) for y in format(ord(x),"08b")] for x in message])          ### to convert data in 8 bit binary
        mess[mess ==0] = -1
        
        mess =mess* -np.pi/2
        #print(mess)
        midchunk = chunksize // 2
        #print(midchunk)

        phases[0,midchunk - mess_len :midchunk] = mess
        phases[0,midchunk+1 : midchunk+1+mess_len] = -mess[::-1]
        #print(phases)

        for i in range(1,len(phases)):                  ##### Inverse Fast Fourier Transformation
            phases[i]=phases[i-1] + phasediff[i-1]

        chunks =(magnitudes*np.exp(1j*phases))
        chunks = np.fft.ifft(chunks).real

        data[0] = chunks.ravel().astype(np.int16)       ### recombing of new data with header to form the encoded wav file
        wavfile.write(path_to_save_file,rate,data.T)
        #final.save(path_to_save)
        
        
        enc_mess = Label(frame,text = "Message Hiding: Success\n Audio Saved: Success")
        enc_mess.config(font = ("Times New Romar",11))
        enc_mess.place(relx = 0.8,rely = 0.50,anchor = CENTER)

        
def phase_decode(frame,path_to_encoded_file):
    rate, data = wavfile.read(path_to_encoded_file)
    
    mess_len =1200               ### assumed
    block_len = 2* int(2**np.ceil(np.log2(2*mess_len)))
    block_mid = block_len//2

    if(len(data.shape) == 1):
        code =data[:block_len]
    else:
        code = data[:block_len,0]

    code_phases = np.angle(np.fft.fft(code))[block_mid - mess_len:block_mid]
    code_in_bits = (code_phases < 0).astype(np.int16)
    code_in_int = code_in_bits.reshape((-1,8)).dot(1<<np.arange(8-1,-1,-1))

    message = "".join(np.char.mod("%c",code_in_int)).replace("`","")

    if(message[-5:]!='$t3g0'):
        message =''

    if(len(message)!=0):
        L2 = Label(frame,text = "Decode Successful \nMessage Found:")
        L2.config(font=("Magneto",11))
        L2.place(relx =0.8, rely =0.43 ,anchor= CENTER)

        output = Label(frame,text =message[0:-5])
        output.config(font=("Times New Roman",12),bd=10)
        output.place(relx=0.8,rely = 0.5 ,anchor = CENTER)

    else:
        L2 = Label(frame,text = "Decode Unsuccessful \n NO Message Found:")
        L2.config(font=("Magneto",11))
        L2.place(relx =0.8, rely =0.43 ,anchor= CENTER)
        
    
    
