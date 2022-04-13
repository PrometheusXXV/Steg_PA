from PIL import Image

def pixel_to_bits(img):
    pixel = list(img.getdata())
    for i in range(len(pixel)):
        pseudo = list(pixel[i])
        for j in range(3):
            temp = pseudo[j]
            pseudo[j] = format(temp,"08b")
        pixel[i] = tuple(pseudo)

    print(pixel[0:10])
    return pixel

def bits_to_pixel(pixel):
    for i in range(len(pixel)):
        pseudo = list(pixel[i])
        for j in range(3):
            temp = pseudo[j]
            pseudo[j] = int(temp,2)
        pixel[i] = tuple(pseudo)

    return(pixel)
    
def merge(img,img_2):
    pixel_bits=[]
    wd,ht = img.size
    pixel_list_1 = pixel_to_bits(img)
    pixel_list_2 = pixel_to_bits(img_2)
    print(len(pixel_list_2))
    for i in range(len(pixel_list_1)):
        pseudo_1 = pixel_list_1[i]
        pseudo_2 = pixel_list_2[i]
        new_pixel = [0,0,0]
        for j in range(3):
            temp_1= pseudo_1[j]
            temp_2= pseudo_2[j]
            new_pixel[j] = temp_1[0:4]+temp_2[0:4]

        pixel_bits.append(tuple(new_pixel))
    pixel = bits_to_pixel(pixel_bits)
    print(pixel[0:10])
    
    pseudo_img = Image.new("RGB",size=(wd,ht))
    for x in range(wd):
        for y in range(ht):
            pseudo_img.putpixel((x,y),pixel[(y*wd+x)])

    pseudo_img.save("merged.png")
    
def encode():
    path = "test_2.png"
    img = Image.open(path,'r')
    img = img.convert("RGB")
    path_2 = "cover.png"
    img_2 = Image.open(path_2,'r')
    img_2 = img_2.convert("RGB")
    img_2 = img_2.resize((272, 170))
    merge(img,img_2)
    
    #print(img.size)

def split(img):
    pixel_bits = pixel_to_bits(img)
    wd,ht = img.size
    pixel_1 = []
    pixel_2 = []
    for i in range(len(pixel_bits)):
        pseudo = pixel_bits[i]
        new_pixel_1 = [0,0,0]
        new_pixel_2 = [0,0,0]
        for j in range(3):
            temp = pseudo[j]
            new_pixel_1[j] = temp[0:4]+'0000'
            new_pixel_2[j] = temp[4:8]+'0000'

        pixel_1.append(tuple(new_pixel_1))
        pixel_2.append(tuple(new_pixel_2))
    pixel = bits_to_pixel(pixel_1)
    pseudo_img = Image.new("RGB",size=(wd,ht))
    for x in range(wd):
        for y in range(ht):
            pseudo_img.putpixel((x,y),pixel[(y*wd+x)])

    pseudo_img.show()
    pixel = bits_to_pixel(pixel_2)
    pseudo_img = Image.new("RGB",size=(wd,ht))
    for x in range(wd):
        for y in range(ht):
            pseudo_img.putpixel((x,y),pixel[(y*wd+x)])

    pseudo_img.show()

def decode():
    path = "merged.png"
    img = Image.open(path,'r')
    split(img)

decode()
