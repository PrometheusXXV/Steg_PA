import cv2
from PIL import Image, ImageDraw as ID , ImageFont as IF

def getsize(txt, font):
    testimg = Image.new('RGBA',(1,1))
    testdraw = ID.Draw(testimg)
    return (testdraw.textsize(txt,font))


def create_image_from_text(cover):
    message = input("ENTER THE MESSAGE TO MAKE WATERMARK: ")

    fontname = "arial.ttf"
    fontsize = 20

    WD, HT =cover.size
    
    colorText = "red"
    colorOutline = "red"
    ColorBackground = "white"

    font = IF.truetype(fontname,fontsize)
    wd, ht = getsize(message,font)

    if(wd<WD  or  ht<HT):
        img  = Image.new("RGBA",(WD,HT),ColorBackground)
        d = ID.Draw(img)
        d.text((20,20),message,fill = colorText , font=font)

    else :
        img = Image.new("RGBA",(100,100),ColorBackground)
        d = ID.Draw(img)
        d.text((20,20),message,fill = colorText , font=font)
        d = d.resize((WD,HT))

    datas =img.getdata()
    newData = []
    for item in datas:
        if item[0] == 255 and item[1] == 255 and item[2] == 255:
            newData.append((255, 255, 255, 0))
        else:
            newData.append((item[0],item[1],item[2],255))

    img.putdata(newData)
    
    img.save("D:\IIT_DHANBAD\CYBERLABS\STEG_PA\watermark.png","PNG")
    img.show()
            

def encode(cover,water):
    h_img, w_img, _ = cover.shape
    center_y = int(h_img/2)
    center_x = int(w_img/2)
    h_wm, w_wm, _ = water.shape
    top_y = center_y - int(h_wm/2)
    left_x = center_x - int(w_wm/2)
    bottom_y = top_y + h_wm
    right_x = left_x + w_wm

    roi = cover[top_y:bottom_y,left_x:right_x]
    result = cv2.addWeighted(roi,1,water,0.3,0)
    cover[top_y:bottom_y, left_x:right_x] = result

    filename = 'D:\IIT_DHANBAD\CYBERLABS\STEG_PA\watermark_encoded.png'
    cv2.imwrite(filename, cover)
    cv2.imshow("Resized Input Image", cover)

cover = Image.open("D:\IIT_DHANBAD\CYBERLABS\STEG_PA\carrier.png")

create_image_from_text(cover)


cover = cv2.imread("D:\IIT_DHANBAD\CYBERLABS\STEG_PA\carrier.png")
water = cv2.imread("D:\IIT_DHANBAD\CYBERLABS\STEG_PA\watermark.png")
encode(cover,water)

