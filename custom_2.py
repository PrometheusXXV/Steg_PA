import wave
import base64

def base_64(message):
    mess_bytes = message.encode("ascii")
    base_64_bytes = base64.b64encode(mess_bytes)
    base_64_str = base_64_bytes.decode('ascii')
    #print(base_64_str)
    return base_64_str[:-2]

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
        
encode()
