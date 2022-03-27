from PIL import Image

def message_to_bits(data):          ### for encoding
    newdata =[]
    newdata= ''.join([format(ord(i), "08b") for i in data])
    return newdata

def next_prime(n):
    i =0
    while(i==0):
        count =0
        for j in range(1,n+1):
            if(n%j==0):
                count += 1

        if(count == 2):
            i+=1
        n+=1
    return (n-1)

def prng_cal(message):
    a = int(input("Seed : "))            ## seed
    c = int(input("Increment : "))       ## increment
    mess_len = len(message)*3
    mod = next_prime(mess_len)
    pixel_list = []
    print(a,c,mod)
    x=1
    y=0
    while(len(pixel_list)<mess_len):
        y = (a*x +c)%mod
        x=y
        if(y<=mess_len and y not in pixel_list):
            pixel_list.append(y)

    return pixel_list
def prng_encode():
    cover = Image.open("D:/IIT_DHANBAD/CYBERLABS/STEG_PA/cover.png",'r')
    cover =cover.convert("RGB")
    wd,ht = cover.size
    message = "ABHI"
    mess_in_bits = message_to_bits(message)
    pix_list = prng_cal(message)
    print(pix_list)
    count =0
    img_pixel = list(cover.getdata())
    for i in range(len(pix_list)):
        a= pix_list[i]
        print(a)
        pseudo = list(img_pixel[a])
        print(pseudo)
        if(i%3==1):
            pseudo[2] = int(format(pseudo[2],"08b")[0:6]+ mess_in_bits[count:count+2],2)        
            count +=2
        else:
            pseudo[2] = int(format(pseudo[2],"08b")[0:6]+ mess_in_bits[count:count+2],2)
            count +=2
            pseudo[1] = int(format(pseudo[1],"08b")[0:7]+ mess_in_bits[count:count+1],2)
            count +=1

        img_pixel[a] = tuple(pseudo)
        print(img_pixel[a])

    for x in range(wd):
        for y in range(ht):
            cover.putpixel((x,y),img_pixel[(y*wd+x)])

    cover.show()
#cover.show()

prng_encode()
