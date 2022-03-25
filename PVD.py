#!/usr/bin/env python3

from PIL import Image


def range_l_u(diff):
    if(diff>=0 and diff<8):
        l=0;u=7;bit_no=3
    elif(diff>=8 and diff<16):
        l=8;u=15;bit_no=3
    elif(diff>=16 and diff<32):
        l=16;u=31;bit_no=4
    elif(diff>=32 and diff<64):
        l=32;u=63;bit_no=5
    elif(diff>=64 and diff<128):
        l=64;u=127;bit_no=6
    elif(diff>=128 and diff<256):
        l=128;u=255;bit_no=7

    return u,l,bit_no

def new_value(a,b,m,diff_1,diff_2):
    if(a>=b and diff_2>diff_1):
        a_new = a+int(m/2) ; b_new = b-int(m/2)
    if(a<b and diff_2>diff_1):
        a_new = a+int(m/2) ; b_new = b-int(m/2)
    if(a>=b and diff_2<=diff_1):
        a_new = a+int(m/2) ; b_new = b-int(m/2)
    if(a<b and diff_2<=diff_1):
        a_new = a+int(m/2) ; b_new = b-int(m/2)

    return a_new ,b_new

    
def message_to_bits(data):          ### for encoding
    newdata = []
    newdata = ''.join([format(ord(i), "08b") for i in data])
    return newdata

def pvd_encode(cover,message):
    data=message_to_bits(message)
    len_data = len(data)
    wd ,ht = cover.size
    pixel = list(cover.getdata())
    total_pixel = len(pixel)
    #print(pixel)
    counter = 0
    print(data)
    print(total_pixel)
    
    for i in range(0,len_data,2):
        if(data.isnumeric()):
            print(i)
            a = pixel[i]
            diff_1 = abs(a[0] - a[1])
            diff_2 = abs(a[1] - a[2])
            upper_1, lower_1, no_of_bits_1 = range_l_u(diff_1)
            need_1 = data[0:no_of_bits_1]
            #print(data)
            #print(no_of_bits_1)
            if(need_1.isnumeric()):
                need_dec= int(need_1,2)
                data = data[no_of_bits_1:]
                diff_1_2 = lower_1+need_dec
                m = abs(diff_1-diff_1_2)
                r1,g1 = new_value(a[0],a[1],m,diff_1,diff_1_2)
            else:
                break
            upper_2, lower_2, no_of_bits_2 = range_l_u(diff_2)
            need_2 = data[0:no_of_bits_2]
            #print(data)
            #print(no_of_bits_1)
            if(need_2.isnumeric()):
                need_dec= int(need_2,2)
                data = data[no_of_bits_2:]
                diff_2_2 = lower_2+need_dec
                m = abs(diff_2-diff_2_2)
                g2,b1 = new_value(a[1],a[2],m,diff_2,diff_2_2)
            else:
                break
            g_final = int((g1+g2)/2)
            g_diff = int((abs(g1-g2))/2)
            
            r_final = r1-g_diff
            b_final = b1+g_diff

            pixel[i]=(r_final,g_final,b_final)
        else:
            break
    for x in range(wd):
        for y in range(ht):
            cover.putpixel((x,y),pixel[(y*wd+x)])          
    return cover
             
    
cover = Image.open("D:\IIT_DHANBAD\CYBERLABS\STEG_PA\message.png")
message=input("Enter the message : ")

cover.convert("RGB")
print(cover.size)

cover_2 = pvd_encode(cover,message)
cover_2.show()

#cover.show()
