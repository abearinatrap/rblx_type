import cv2
import pytesseract
import numpy as np
from mss import mss
import time
#img = cv2.imread("images/me.jpg")
stc = mss()
def cameraCap():
    capture = cv2.VideoCapture(0)
    capture.set(3,640)
    capture.set(4,480)
    capture.set(10,100)
    while True: 
        success, img = capture.read()
        cv2.imshow("Video",img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

def Screen_Shot(left=0, top=0, width=1920, height=1080):
    scr = stc.grab({
        'left': left,
        'top': top,
        'width': width,
        'height': height
    })

    img = np.array(scr)
    img = cv2.cvtColor(img, cv2.IMREAD_COLOR)
    #for i in range(4):
    #    stc.shot(output=f"mon-{i}.png")
    #    time.sleep(1)
    return img

def stillImage():
    cv2.line(img,(0,0),(20,50),(5,5,5),3)
    print(img.shape)
    cv2.imshow("Test",img[70:450,470:800])
    cv2.waitKey(0)

def showImage(img,name):
    cv2.imshow(name,img)
    cv2.waitKey(0)

def boundaryColor(image,boundaries):
    pass
#filename = stc.shot()
# hex code of box color is 1ac6ff
#   through 1cc7ff
#only one boundary but set up so to have multiple boundary masks
#numpy is bgr instead of rgb
boundaries=[([250,195,26],[255,200,32])]

img = cv2.imread("screeny.png")
for (low, high) in boundaries:
    lower=np.array(low,dtype="uint8")
    higher=np.array(high,dtype="uint8")
    mask=cv2.inRange(img,lower,higher)
    output=cv2.bitwise_and(img,img,mask=mask)
    #showImage(img,"image") 
    #showImage(mask,"mask")
    #showImage(output,"mask for color of edge")
    contours,hierarchy= cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    rect=cv2.minAreaRect(contours[0])
    box=cv2.boxPoints(rect)
    box=np.int0(box)
    print(box)
    #get min point and max point
    min_x,min_y=255,255
    max_x,max_y=0,0
    for [x,y] in box:
        min_x=min(min_x,x)
        max_x=max(max_x,x)
        min_y=min(min_y,y)
        max_y=max(max_y,y)
    box_rect=[[min_x,min_y],[max_x,min_y],[max_x,max_y],[min_x,max_y]]
    box_rect=np.int0(box_rect)
    #rect2=cv2.drawContours(img,[box_rect],0,(0,255,0),3)
    #showImage(rect2,"rect")

matrix=cv2.getPerspectiveTransform(box.astype(np.float32),box_rect.astype(np.float32))
print(img.shape)
result=cv2.warpPerspective(img,matrix,(img.shape[1],img.shape[0]))
showImage(result,"results")
boundedimg=img[min_y:max_y,min_x:max_x]
showImage(boundedimg,"bounded iamge")
mask_letter=cv2.inRange(boundedimg,np.array([0,0,0],dtype="uint8"),np.array([70,50,30],dtype="uint8"))
output=cv2.bitwise_and(boundedimg,boundedimg,mask=mask_letter)
showImage(output,"output letter")
print("text: "+pytesseract.image_to_string(mask_letter))
#print(pytesseract.image_to_string(cv2.imread("monitor-1.png")))
#cv2.drawContours(img,[cnt],0,(0,255,0),3)
#print(filename)
#cameraCap()
#showImage(Screen_Shot(100,600,500,300),"screenshot")
#print(stc.shot())
#print(img)

print(cv2.imread("mon-0.png").shape)
#showImage(cv2.imread("mon-0.png"),"rblx img")
