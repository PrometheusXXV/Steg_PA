#PN sequence generator   takes a seed and used for encryption 
#direct message or first conversion into base64 and then to 8 bit binary
#combining above both

#cover audio --->>> frames  ---->>> message embedded in center of the cover audio
#embedding is done by LSB method 

import base64
import wave

def split(word):
    return [char for char in word]

def pn_seq(l,seed):            #### PN sequence generator
    key_1 =[]
    mess_byte_len =int(l/8)
    seed_l=len(seed)
    #print(mess_byte_len)
    final_seed = seed*(mess_byte_len//seed_l)+seed[0:mess_byte_len%seed_l]
    final_bits= ''.join([format(ord(i), "08b") for i in final_seed])   
    final_bits = split(final_bits)
    return final_bits

def base_64(message):
    mess_bytes = message.encode("ascii")
    base_64_bytes = base64.b64encode(mess_bytes)
    base_64_str = base_64_bytes.decode('ascii')
    #print(base_64_str)
    return base_64_str[:-2]

def bit_encode(message):
    newdata = []
    newdata =''.join([format(ord(i), "08b") for i in message])
    new_data=[]
    #print(newdata)
    newdata = split(newdata)

    return newdata

def frame_encoding(frames,message,pn):
    l = len(frames)
    frame_new =[]
    for i in range(l):
        frame_bytes = bin(frames[i])
        if(message[i] == pn [i]):
            fb_mod = frame_bytes[2:9]+'1'
        else:
            fb_mod = frame_bytes[2:9]+'0'
        frame_new.append(int(fb_mod,2))

    return frame_new

def spread_encode():
    path_to_file = input("Enter the path to wav_file :")
    message = input("Enter the message to hide :")
    seed = input("Enter the seed for encryption :")
    #rate, data = wavfile.read(path_to_file)
    cover = wave.open(path_to_file,mode = 'r')
    frame_len = cover.getnframes()
    cover_frames = list(cover.readframes(frame_len))
    #print(cover_frames[0:2000])
    #print(cover.getnchannels())
    #print(data[0:1000])
    mid_frame = frame_len//2
    #print(mid_frame,frame_len)
    mess_data = bit_encode(base_64(message))
    mess_len = len(mess_data)
    pn_data = pn_seq(mess_len,seed)
    #print(len(pn_data))
    req_frames = cover_frames[(mid_frame-int(mess_len/2)):(mid_frame+int(mess_len/2))]
    #print(len(req_frames))
    #print(req_frames)
    new_frames=frame_encoding(req_frames,mess_data,pn_data)
    #print(new_frames)

    for i in range(len(new_frames)):
        cover_frames[(mid_frame-int(mess_len/2))+i] =new_frames[i]

    cover_frames_bytes =bytes(cover_frames)
    with wave.open('cover_custom_embed.wav','w') as final:
        final.setparams(cover.getparams())
        final.writeframes(cover_frames_bytes)

    cover.close()
    
spread_encode()
#bit_encode("Abhinav")     
#print(base_64("Abhinav"))
#pn_seq(80,"abcd")
