import os.path

import numpy as np
from scipy.io import wavfile


def form_chuck():
    pass

def phase_encode():
    path_to_file = input("Enter the path to wav_file :")
    message = input("Enter the message to encode :")
    rate, data_1 = wavfile.read(path_to_file)

    message = message.ljust(150,'#')            #### can store message of 150 bytes for easier decoding
    mess_len = 8*len(message)
    chunksize = int(2*2**np.ceil(np.log2(2*mess_len)))
    #print(chunksize)
    number_of_chunks = int(np.ceil(data_1.shape[0]/chunksize))
    print(data_1.shape)
    print(number_of_chunks)

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
    print(mess)

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
    dir = os.path.dirname(path_to_file)
    wavfile.write(dir+"/encoded_pc.wav",rate,data.T)

def phase_decode():
    path_to_encoded_file = input("Enter the path to encoded wav_file :")
    rate, data = wavfile.read(path_to_encoded_file)

    mess_len =1200               ### assumed
    block_len = 2* int(2**np.ceil(np.log2(2*mess_len)))
    block_mid = block_len//2
    print(block_len,block_mid)

    if(len(data.shape) == 1):
        code =data[:block_len]
    else:
        code = data[:block_len,0]
    print(code)

    code_phases = np.angle(np.fft.fft(code))[block_mid - mess_len:block_mid]
    code_in_bits = (code_phases < 0).astype(np.int16)
    code_in_int = code_in_bits.reshape((-1,8)).dot(1<<np.arange(8-1,-1,-1))

    message = "".join(np.char.mod("%c",code_in_int)).replace("#","")
    print(message)
    
phase_decode()
