from PIL import Image, ImageDraw, ImageFont
import cv2

def getsize(txt,font):
    testimg=Image.new('RGB',(1,1))
    testdraw =ImageDraw.Draw(testimg)
    return (testdraw.textsize(txt,font))

fontname = "arial.ttf"
fontsize =14
text = "Abhinav"

colorText="black"
colorOutline = "red"
ColorBackground = "white"

base=cv2.imread("D:\IIT_DHANBAD\CYBERLABS\STEG_PA\carrier.png")

font = ImageFont.truetype(fontname,fontsize)
width, height = getsize(text,font)
img = Image.new('RGB', (width+4,height+4),ColorBackground)
d= ImageDraw.Draw(img)
d.text((2,2),text, fill =colorText , font=font) #draws text 
d.rectangle((0,0,width+3,height+3),outline=colorOutline) # draws a rectangle

img.save("D:\IIT_DHANBAD\CYBERLABS\STEG_PA\message.png")


watermark =cv2.imread("D:\IIT_DHANBAD\CYBERLABS\STEG_PA\message.png")


dim=watermark.shape
dim2 =base.shape
if(base.shape[0]< dim[0]  or  base.shape[1] < dim[1]):
    resized_wm = cv2.resize(watermark, (int(base.shape[1]*30/100),int(base.shape[0]*30/100)))
else:
    resized_wm = cv2.resize (watermark,(dim[1],dim[0]))

filename = "D:\IIT_DHANBAD\CYBERLABS\STEG_PA\watermark.png"

center_y,center_x ,_ =base.shape
h_wm, w_wm, _ = resized_wm.shape
top_y = center_y - int(h_wm/2)
left_x = center_x - int(w_wm/2)
bottom_y = top_y + h_wm
right_x = left_x + w_wm
#img = cv2.addWeighted(source1, alpha, source2, beta, gamma[, dst[, dtype]])
roi = base[top_y:bottom_y, left_x:right_x]

result = cv2.addWeighted(roi, 1, resized_wm, 0.3, 0)


cv2.imwrite("D:\IIT_DHANBAD\CYBERLABS\STEG_PA\Crypted.png", result)
print(dim)

cv2.imshow("Resized Input Image", result)
