import wave
import base64
from tkinter import *

def base_64(message):
    mess_bytes = message.encode("ascii")
    base_64_bytes = base64.b64encode(mess_bytes)
    base_64_str = base_64_bytes.decode('ascii')
    #print(base_64_str)
    return base_64_str

def base_64_decode(message):
    try:
        byte_mess = base64.b64decode(message)
        return byte_mess.decode('utf8')
    except Exception:
        return "aaaa"

    
def encry_xor(s1,s2):        ######XOR encrytption 
    xor_mess = [ord(a) ^ ord(b) for a,b in zip(s1,s2)]
    return xor_mess 

def frame_encode(req_frames, message):
    new_frame = []
    for i in  range(len(message)):
        new_frame.append(int(bin(req_frames[i])[2:9]+message[i],2))

    return (new_frame)
    
    
def pn_seq(l,seed):
    key = ''
    seed_l = len(seed)
    key = seed*(l//seed_l)+ seed[0:l%seed_l]
    return key

def message_to_bits(data):          ### for encoding
    newdata = []
    newdata = ''.join([format(i, "08b") for i in data])
    return newdata


def decrypt_xor(s1,list1):
    xor_mess = [ord(a) ^ b for a,b in zip(s1,list1)]
    return xor_mess

def custom_encode(message_input, frame, seed_input,save_path,path_to_file):
    message = message_input.get(1.0,'end-1c')
    if(len(message)!=0):
        message = message + "$t3g0"
    seed = seed_input.get(1.0,'end-1c')
    path_to_save_file = save_path.get(1.0,'end-1c')

    if(len(path_to_file)==0):
        L4 = Label(frame,text = "No Audio File Selected")
        L4.config(font = ("Times New Roman",12))
        L4.place(relx = 0.2,rely =0.5,anchor =CENTER)
    elif(len(message) == 0):
        L4 = Label(frame,text = "No Message Entered \n Enter the Message to Hide")
        L4.config(font = ("Times New Roman",12))
        L4.place(relx = 0.5,rely =0.3,anchor =CENTER)
    elif(len(seed)==0):
        L5 = Label(frame,text = "Enter the seed(word)\nfor encryption\nof the message")
        L5.config(font = ("Times New Roman",12))
        L5.place(relx=0.5,rely=0.57,anchor=CENTER)
    elif(len(path_to_save_file)==0):
        L5 = Label(frame,text = "Enter the file name \nto save the encoded file \nto procedd")
        L5.config(font = ("Times New Roman",12))
        L5.place(relx=0.8,rely=0.35,anchor=CENTER)
    else:
        cover = wave.open(path_to_file,mode ='r')
        frame_len =cover.getnframes()
        cover_frames = list(cover.readframes(frame_len))
        mid_frame = frame_len //2
        mess_b64 = base_64(message)

        mess_b64_len = len(mess_b64)

        pn_data = pn_seq(mess_b64_len,seed)

        final_message = encry_xor(mess_b64,pn_data)

        bits_message = message_to_bits(final_message)
        length = len(bits_message)
        start =mid_frame -int(length/2)
        req_frames = cover_frames[start:start+length]
        #print(req_frames)
        
        #print(bits_message)
        new_frames = frame_encode(req_frames,bits_message)

        for i in range(len(req_frames)):
            cover_frames[start+i] = new_frames[i]

        cover_frames_bytes =bytes(cover_frames)
        with wave.open(path_to_save_file,'w') as final:
            final.setparams(cover.getparams())
            final.writeframes(cover_frames_bytes)

        cover.close()
        enc_mess = Label(frame,text = "Message Hiding: Success\n Audio Saved: Success")
        enc_mess.config(font = ("Times New Romar",11))
        enc_mess.place(relx = 0.8,rely = 0.50,anchor = CENTER)

def custom_decode(frame,seed_input,path_to_file):
    
    seed = seed_input.get(1.0,'end-1c')
    if(len(seed) == 0):
        L5 = Label(frame,text = "Enter the seed(word)\nfor decryption\nof the message")
        L5.config(font = ("Times New Roman",12))
        L5.place(relx=0.5,rely=0.57,anchor=CENTER)
    else:    
        encoded_file = wave.open(path_to_file,mode = 'r')
        frame_len = encoded_file.getnframes()
        cover_frames = list(encoded_file.readframes(frame_len))
        mid_frame = frame_len//2
        decry = ''
        counter = 1
        
        while(decry[-5:] !='$t3g0' and counter< 100 ):
            pseudo_len = 8*counter
            mess = ''
            start = mid_frame-int(pseudo_len/2)
            encoded_frame = cover_frames[start:(start+pseudo_len)]
            for k in range(len(encoded_frame)):
                a = format(encoded_frame[k],"08b")
                mess += a[-1]
            #print(mess)
            xor_en =[]
            for k in range(counter):
                data = mess[8*k:8*(k+1)]
                #print(data)
                if(data!= ''):
                    xor_en.append(int(data,2))
            final_seed =pn_seq(counter,seed)
            #print(xor_en)
            decode_list = decrypt_xor(final_seed,xor_en)
            #print(decode_list)
            final = ''
            for j in range(len(decode_list)):
                final += chr(int(decode_list[j]))
            #print(final)
            #print(len(final))
            
            if(len(final)%4==0):
                decry = base_64_decode(final)
            print(decry)
            counter +=1
        if(decry[-5:]!="$t3g0"):
            decry =''

        if (len(decry)!= 0):
            L2 = Label(frame,text = "Decode Successful \nMessage Found:")
            L2.config(font=("Magneto",11))
            L2.place(relx =0.8, rely =0.43 ,anchor= CENTER)
                     
            output = Label(frame,text = decry[0:-5])
            output.config(font=("Times New Roman",12),bd=10)
            output.place(relx=0.8,rely = 0.5 ,anchor = CENTER)
        else:
            L2 = Label(frame,text = "Decode Unsuccessful \n NO Message Found:")
            L2.config(font=("Magneto",11))
            L2.place(relx =0.8, rely =0.43 ,anchor= CENTER)
        print("Encrytpted Message was : ", decry[0:-5])
        
