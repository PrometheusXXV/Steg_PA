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

    pseudo_img.show()
    
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
    
    

encode()
