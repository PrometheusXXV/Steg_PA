#!/usr/bin/env python3

from PIL import Image

def message_to_bits(data):          ### for encoding
    newdata = []
    newdata = ''.join([format(ord(i), "08b") for i in data])
    return newdata

def image_to_pixel(image):          #converts images to pixel and returns pixel values 
    pixel=image.load()
    pixel_list = []
    for i in range(image.size[1]):
        for j in range(image.size[0]):
             pixel_list =pixel_list + list(pixel[j,i])
    
    return pixel_list

def modified_pixel(img,data): 
    datalist=message_to_bits(data)
    len_data = len(datalist)
    
    pixel = list(img.getdata())
    total_pixel = len(pixel)

    if(total_pixel<len_data):
        print("ERROR : Need more P1xels")
    else :
        counter =0
        for x in range(total_pixel):
            pseudo = list(pixel[x])
            for y in range(0,3):
                if counter < len_data:
                    pseudo[y] = int(bin(pseudo[y])[2:9]+datalist[counter],2)
                    counter +=1
            pixel[x]=tuple(pseudo)

    return(pixel)
    
def modif_encoded_image(pseudo_img,data):
    wd,ht = pseudo_img.size
        
    pixel = modified_pixel(pseudo_img,data)
    for x in range(wd):
        for y in range(ht):
            pseudo_img.putpixel((x,y),pixel[(y*wd+x)])    
    
def encode_image():
    img  = input("Enter file path with extension:")
    image = Image.open(img,'r')

    data = input("Enter data to encode/hide : ")
    data = data + "$t3g0"

    if (len(data) ==0):
        raise ValueError('Data is Empty')

    pseudo_img = image.copy()
    modif_encoded_image(pseudo_img,data)

    encoded_image_name=input("Enter the name of new image(with extension):")
    pseudo_img.save(encoded_image_name,str(encoded_image_name.split('.')[1].upper()))



def decode_image():
    message = ''

    img =input("Enter file path with extension :")
    image = Image.open(img,'r')
    pixel = list(image.getdata())
    total_pixel = len(pixel)

    hidden_bits =''
    for x in range(total_pixel):
        pseudo = list(pixel[x])
        for y in range(3):
            hidden_bits += (bin(pseudo[y])[2:][-1])

    hidden_bits = [hidden_bits[i:i+8] for i in range(0,len(hidden_bits),8)]

    for i in range(len(hidden_bits)):
        if message[-5:] == "$t3g0":
            break
        else :
            message += chr(int(hidden_bits[i],2))
    print(message[:-5])
          

print("Encode the image")
encode_image()
print("Decode the image")
decode_image()

    
