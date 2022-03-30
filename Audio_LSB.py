import wave

def message_to_bits(data):          ### for encoding
    newdata =[]
    newdata= ''.join([format(ord(i), "08b") for i in data])
    return newdata

def a_lsb_encode(message,song):
    song_frames = list(song.readframes(song.getnframes()))
    mess = message_to_bits(message)
    print(mess)
    print(song_frames[0:20])
    new_song_frames=[]
    for i in range(len(song_frames)):
        if ( i<len(mess)):
            frame_byte = bin(song_frames[i])
            frame_byte_modified = frame_byte[2:9]+mess[i]
            print(frame_byte_modified)
            new_song_frames.append(int(frame_byte_modified,2))
        else:
            new_song_frames.append(song_frames[i])

    print(new_song_frames[0:20])
    frame_modified_final = bytes(new_song_frames)
    with wave.open('song_embedded.wav','w') as final:
        final.setparams(song.getparams())
        final.writeframes(frame_modified_final)

    song.close()
    
song = wave.open("D:/IIT_DHANBAD/CYBERLABS/STEG_PA/testing.wav",mode = 'r')
message = input("Enter the message to encode :")

a_lsb_encode(message,song)
