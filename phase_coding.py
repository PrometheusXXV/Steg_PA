import os.path

import numpy as np
from scipy.io import wavfile


def form_chuck():
    pass

def phase_encode():
    path_to_file = input("Enter the path to wav_file :")
    message = input("Enter the message to encode :")
    rate, data_1 = wavfile.read(path_to_file)
    print(rate)
    mess_len = 8*len(message)
    chunksize = int(2*2**np.ceil(np.log2(2*mess_len)))
    #print(chunksize)
    number_of_chunks = int(np.ceil(data_1.shape[0]/chunksize))
    print(data_1.shape)
    print(number_of_chunks)
    data = data_1.copy()

    if(len(data_1.shape)==1):
        data.resize(number_of_chunks*chunksize)
        data = data[np.newaxis]
        print(data.shape)

    else:
        data.resize((number_of_chunks*chunksize,data.shape[1]))
        data =data.T     #### transpose the array
        #print(data.shape)

    chunks = data[0].reshape((number_of_chunks, chunksize))

    chunks = np.fft.fft(chunks)
    magnitudes =np.abs(chunks)
    phases =np.angle(chunks)
    phasediff = np.diff(phases,axis=0 )

    
    mess = np.ravel([[int(y) for y in format(ord(x),"08b")] for x in message])
    mess[mess ==0] = -1
    print(mess)

    mess =mess* -np.pi/2
    print(mess)
    midchunk = chunksize // 2
    print(midchunk)

    phases[0,midchunk - mess_len :midchunk] = mess
    phases[0,midchunk+1 : midchunk+1+mess_len] = -mess[::-1]
    print(phases)

    for i in range(1,len(phases)):
        phases[i]=phase[i-1] + phasediff[i-1]

    chunks =(magnitudes*np.ex(1j*phases))
    chunks = no.fft.ifft(chunks).real
phase_encode()
