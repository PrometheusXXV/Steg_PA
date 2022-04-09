from PIL import Image
from math import floor,ceil

def message_to_bits(data):          ### for encoding
    newdata = []
    newdata.append([format(ord(i), "08b") for i in data])
    return newdata[0]

def new_value(prev_1,prev_2,dr,db,dg):
    new_1=[0,0,0]
    new_2=[0,0,0]
    val_r = int(dr,2)
    change_r_1 = floor(val_r/2)
    change_r_2 = ceil(val_r/2)
    new_1[0] =int(format(prev_1[0],"08b")[0:5]+format(change_r_1,"08b")[-3:],2)
    new_2[0] =int(format(prev_2[0],"08b")[0:5]+format(change_r_2,"08b")[-3:],2)
    
    val_g = int(dg,2)
    change_g_1 = floor(val_g/2)
    change_g_2 = ceil(val_g/2)
    new_1[1] = int(format(prev_1[1],"08b")[0:5]+(format(change_g_1,"08b")[-3:]),2)
    new_2[1] = int(format(prev_2[1],"08b")[0:5]+(format(change_g_2,"08b")[-3:]),2)

    val_b = int(db,2)
    change_b_1 = floor(val_b/2)
    change_b_2 = ceil(val_b/2)
    new_1[2] = int(format(prev_1[2],"08b")[0:6]+(format(change_b_1,"08b")[-2:]),2)
    new_2[2] = int(format(prev_2[2],"08b")[0:6]+(format(change_b_2,"08b")[-2:]),2)
    
    print(val_r,val_g,val_b)
    return tuple(new_1),tuple(new_2)

def pvd_encode(cover,message):
    data = message_to_bits(message)
    len_data = len(data)

    wd, ht = cover.size
    pixel =list(cover.getdata())
    total_pixel=len(pixel)

    for i in range(len_data):
        a = pixel[2*i]
        b = pixel[2*i+1]
        print(a,b)
        ###### R mein 3
        ###### B mein 2
        ###### G mein 3

        pseudo =data[i]
        #print(pseudo)
        dr = pseudo[0:3]
        dg = pseudo[3:6]
        db = pseudo[6:]
        a_new,b_new = new_value(a,b,dr,db,dg)
        
        pixel[2*i] = a_new
        pixel[(2*i)+1] = b_new

    for x in range(wd):
        for y in range(ht):
            cover.putpixel((x,y),pixel[(y*wd+x)])

    return cover

def pvd_decode(cover):
    pixel = list(cover.getdata())
    total_pixel =len(pixel)
    counter = 0 
    message =''
    while(message[-5:]!="$t3g0"):
        
        a= pixel[2*counter]
        b= pixel[2*counter+1]
        mess =''
        for j in range(3):
            if(j==0 or j==1):
                x = int(format(a[j],"08b")[-3:],2)
                y = int(format(b[j],"08b")[-3:],2)
                req =x+y
                mess += format(req,"08b")[-3:]
            else:
                x = int(format(a[j],"08b")[-2:],2)
                y = int(format(b[j],"08b")[-2:],2)
                req =x+y
                mess += format(req,"08b")[-2:]

        message += chr(int(mess,2))
        counter += 1

    print(message[0:-5])
        
#print(message_to_bits("ABHINAV"))
cover = Image.open("D:\IIT_DHANBAD\CYBERLABS\STEG_PA\message.png")
message=input("Enter the message : ")
message = message+"$t3g0"
cover.convert("RGB")
cover_2 = pvd_encode(cover,message)
cover_2.save("D:\IIT_DHANBAD\CYBERLABS\STEG_PA\pvd_encoded.png")


xyz = Image.open("D:\IIT_DHANBAD\CYBERLABS\STEG_PA\pvd_encoded.png")
pvd_decode(xyz)


