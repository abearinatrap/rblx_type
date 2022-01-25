import cv2

import numpy as np
from mss import mss
import time
img = cv2.imread("images/me.jpg")
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
    for i in range(4):
        stc.shot(output=f"mon-{i}.png")
        time.sleep(1)
    return img

def stillImage():
    cv2.line(img,(0,0),(20,50),(5,5,5),3)
    print(img.shape)
    cv2.imshow("Test",img[70:450,470:800])
    cv2.waitKey(0)

#filename = stc.shot()
#print(filename)
#cameraCap()
Screen_Shot()