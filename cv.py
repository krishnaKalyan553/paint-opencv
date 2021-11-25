import numpy as np
import cv2 as cv
color=(0,255,255)
def empty(self):
    pass
drawing=False
img=np.zeros((600,600,3),np.uint8)
blank=np.full_like(img,200)
cv.namedWindow('paint',cv.WINDOW_NORMAL)
cv.namedWindow('pick color',cv.WINDOW_NORMAL)
cv.createTrackbar("B",'pick color',0,255,empty)
cv.createTrackbar("G",'pick color',0,255,empty)
cv.createTrackbar("R",'pick color',0,255,empty)
def draw(event,x,y,flags,param):
    global color
    if event==cv.EVENT_LBUTTONDOWN:
        cv.circle(blank,(x,y),2,(255,0,0),-1)
        global drawing
        drawing=True
    if event==cv.EVENT_LBUTTONUP:
        drawing=False
    elif event==cv.EVENT_MOUSEMOVE:
        if drawing==True:
            cv.circle(blank,(x,y),5,color,-1)


cv.setMouseCallback('paint',draw)
while(1):
    cv.imshow('paint',blank)
    k = cv.waitKey(1) & 0xFF
    B=cv.getTrackbarPos('B','pick color')
    G=cv.getTrackbarPos('G','pick color')
    R=cv.getTrackbarPos('R','pick color')
    color=(B,G,R)
    if k==27:
        break
    if k==ord('q'):
        blank=np.full_like(img,200)
    if k==ord('s'):
        cv.imwrite('canvas.jpg',blank)
    