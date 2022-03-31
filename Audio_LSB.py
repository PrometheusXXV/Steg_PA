import wave

def message_to_bits(data):          ### for encoding
    newdata =[]
    newdata= ''.join([format(ord(i), "08b") for i in data])
    return newdata

def a_lsb_encode():
    song = wave.open("D:/IIT_DHANBAD/CYBERLABS/STEG_PA/testing.wav",mode = 'r')
    message = input("Enter the message to encode :")
    song_frames = list(song.readframes(song.getnframes()))
    message = message + "$t0p"              ### added to stop the read of code when decrypting
    mess = message_to_bits(message)
    print(mess)
    print(song_frames[0:100])
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
    with wave.open('song_embedded.wav','w') as final:
        final.setparams(song.getparams())
        final.writeframes(frame_modified_final)

    song.close()

def dec_8b(enc_8b):
    x = int(enc_8b,2)
    return chr(x)

def a_lsb_decode():
    enc_message =''
    song = wave.open("D:/IIT_DHANBAD/CYBERLABS/STEG_PA/song_embedded.wav",mode = 'r')
    song_frames = list(song.readframes(song.getnframes()))
    mess = ''
    for i in range(len(song_frames)):
        if(enc_message[-4:] != "$t0p"):
            frame_bytes = bin(song_frames[i])
            mess =mess + frame_bytes[-1]
            if(len(mess)==8):
                enc_message = enc_message + dec_8b(mess)
                mess =''
    print(enc_message[:-4])  

a_lsb_encode()
a_lsb_decode()
