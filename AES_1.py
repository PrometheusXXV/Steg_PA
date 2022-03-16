from random import *
from Crypto.Cipher import AES

char_list = ''.join(chr(i) for i in range (32,127))
print(char_list)
def random_key():
    key=''.join(str(choice(char_list)) for i in range(16))
    return key.encode("utf8")

def in_vec():
    iv = ''.join(str(choice(char_list)) for i in range(16))
    return iv.encode("utf8")

#random_key()    #random key generator
#in_vec()        #initialization vector -> used with key to fail the crypanalysis
               #                       generated with every encryption


key=random_key()
iv=in_vec()
aes = AES.new(key,AES.MODE_CBC,iv)   # in python encode is used

data = input()
#key = input("MUST be 16 byte length:")
#iv = input("MUST be 16 byte length:")
d=0
len_data=len(data)
if(len_data%16!=0):
    d=len_data%16
    data= data + ('@'*(16-d))

print(d)
encd= aes.encrypt(data.encode())

obj2 = AES.new(key,AES.MODE_CBC,iv)   # in python encode is used

dec = obj2.decrypt(encd).decode()
dec = dec[0:len(dec)-(16-d)]
print(dec)


def AES_encrypt():
    pass

def AES_decrpyt():
    pass
