import cv2 as cv
import numpy as np

cap=cv.VideoCapture('/Users/asmitabasak/Desktop/Contact_Detection/beyblade.mp4')
# ret,frame=cap.read()
# def nothing(a):
#     pass
# cv.namedWindow('Trackbar')
# cv.resizeWindow('Trackbar',640,300)
# cv.createTrackbar('B Min','Trackbar',82,255,nothing)
# cv.createTrackbar('B Max','Trackbar',255,255,nothing)
# cv.createTrackbar('G Min','Trackbar',0,255,nothing)
# cv.createTrackbar('G Max','Trackbar',84,255,nothing)
# cv.createTrackbar('R Min','Trackbar',0,255,nothing)
# cv.createTrackbar('R Max','Trackbar',57,255,nothing)

# while True:
#     # frameHSV=cv.cvtColor(frame,cv.COLOR_BGR2HSV)
#     h_min=cv.getTrackbarPos('B Min','Trackbar')
#     h_max=cv.getTrackbarPos('B Max','Trackbar')
#     s_min=cv.getTrackbarPos('G Min','Trackbar')
#     s_max=cv.getTrackbarPos('G Max','Trackbar')
#     v_min=cv.getTrackbarPos('R Min','Trackbar')
#     v_max=cv.getTrackbarPos('R Max','Trackbar')
#     lower=np.array([h_min,s_min,v_min])
#     upper=np.array([h_max,s_max,v_max])
#     mask=cv.inRange(frame,lower,upper)
#     imgRes=cv.bitwise_and(frame,frame,mask=mask)
#     cv.imshow('frame',frame)
#     # cv.imshow('frameHSV',frameHSV)
#     cv.imshow('mask',mask)
#     cv.imshow('result',imgRes)
#     cv.waitKey(1)
def getContours(img,frame):
    contours,hierarchies=cv.findContours(img,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE)
    blank=np.zeros(img.shape,dtype='uint8')
    for cnt in contours:
        cv.drawContours(blank,cnt,-1,(255,255,255),1)
        area=cv.contourArea(cnt)
        if area>1700:
            x,y,w,h=cv.boundingRect(cnt)
            cv.rectangle(frame,(x,y),(x+w+15,y+h+15),(255,255,255),2)  
        cv.imshow('Contours',frame)

# def getContours2(img,frame):
#     contours,hierarchies=cv.findContours(img,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE)
#     blank=np.zeros(img.shape,dtype='uint8')
#     for cnt in contours:
#         cv.drawContours(blank,cnt,-1,(255,255,255),1)
#         area=cv.contourArea(cnt)
#         if area>1700:
#             x,y,w,h=cv.boundingRect(cnt)
#             cv.rectangle(frame,(x,y),(x+w+20,y+h+30),(255,255,255),2)
#         # cv.imshow('Contours',frame)
#     return frame

while True:
    ret,frame=cap.read()
    frame=frame[80:,150:1090]
    # frame=cv.GaussianBlur(frame,(7,7),2)
    lower1=np.array([82,0,0])
    upper1=np.array([255,84,57])
    mask1=cv.inRange(frame,lower1,upper1)
    imgRes1=cv.bitwise_and(frame,frame,mask=mask1)
    lower2=np.array([0,50,18])
    upper2=np.array([98,255,54])
    mask2=cv.inRange(frame,lower2,upper2)
    imgRes2=cv.bitwise_and(frame,frame,mask=mask2)
    res=cv.bitwise_xor(imgRes1,imgRes2)
    kernel=np.ones((5,5),np.uint8)
    res=cv.dilate(res,kernel,iterations=3)
    # res1=cv.dilate(imgRes1,kernel,iterations=3)
    # res2=cv.dilate(imgRes2,kernel,iterations=3)
    imgCanny=cv.Canny(res,50,100)
    # imgCanny1=cv.Canny(res1,50,100)
    # imgCanny2=cv.Canny(res2,50,100)
    # res=cv.bitwise_or(getContours1(imgCanny1,frame),getContours2(imgCanny2,frame))
    # res=cv.bitwise_xor(frame,res)
    getContours(imgCanny,frame)
    # cv.imshow('frame',res)
    # cv.imshow('result1',imgRes1)
    # cv.imshow('result2',imgRes2)
    if cv.waitKey(1) & 0xFF==ord('q'):
        break
cap.release()
cv.destroyAllWindows()
