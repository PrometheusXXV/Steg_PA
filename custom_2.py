import wave
import base64

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

def encode():
    path_to_file = input("Enter the path to wav_file :")
    message = input("Enter the message to hide :")
    message = message + "$t3g0"
    seed = input("Enter the seed for encryption :")

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
    with wave.open('cover_custom_embed.wav','w') as final:
        final.setparams(cover.getparams())
        final.writeframes(cover_frames_bytes)

    cover.close()

def decrypt_xor(s1,list1):
    xor_mess = [ord(a) ^ b for a,b in zip(s1,list1)]
    return xor_mess

def decode():
    path_to_file = input("Enter the path to wav_file :")
    seed = input("Enter the seed for decryption :")
    encoded_file = wave.open(path_to_file,mode = 'r')
    frame_len = encoded_file.getnframes()
    cover_frames = list(encoded_file.readframes(frame_len))
    mid_frame = frame_len//2
    decry = ''
    counter = 1
    
    while(decry[-5:] !='$t3g0'):
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
        #print(decry)
        counter +=1

    print("Encrytpted Message was : ", decry[0:-5])
        

decode()
