import cv2
import numpy as np
import os   
from time import time , clock
from windowcapture_tibia import WindowCapture
from matplotlib import pyplot as plt
import pyautogui

def nothing(x):
    pass
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# WindowCapture.list_window_names()
# exit()
# initialize the WindowCapture class
wincap = WindowCapture('Return Of The Saiyans')

loop_time = time()

cv2.namedWindow("Trackbars")
cv2.createTrackbar("L-H", "Trackbars", 74,180, nothing)
cv2.createTrackbar("L-S", "Trackbars", 88,255, nothing)
cv2.createTrackbar("L-V", "Trackbars", 176,255, nothing)
cv2.createTrackbar("U-H", "Trackbars", 180,180, nothing)
cv2.createTrackbar("U-S", "Trackbars", 255,255, nothing)
cv2.createTrackbar("U-V", "Trackbars", 255,255, nothing)

cv2.namedWindow("Trackpixel")
cv2.createTrackbar("X1", "Trackpixel", 331,1000, nothing)
cv2.createTrackbar("X2", "Trackpixel", 400,1000, nothing)
cv2.createTrackbar("Y1", "Trackpixel", 858,1000, nothing)
cv2.createTrackbar("Y2", "Trackpixel", 938,1000, nothing)
cv2.createTrackbar("XAUX", "Trackpixel", 45,100, nothing)
cv2.createTrackbar("YAUX", "Trackpixel", 70,100, nothing)
while(True):
    screenshot = wincap.get_screenshot()
    #print('FPS {}'.format(1 / (time() - loop_time)))
    loop_time = time()

    l_h = cv2.getTrackbarPos("L-H", "Trackbars")
    l_s = cv2.getTrackbarPos("L-S", "Trackbars")
    l_v = cv2.getTrackbarPos("L-V", "Trackbars")
    u_h = cv2.getTrackbarPos("U-H", "Trackbars")
    u_s = cv2.getTrackbarPos("U-S", "Trackbars")
    u_v = cv2.getTrackbarPos("U-V", "Trackbars")
    x1 = cv2.getTrackbarPos("X1", "Trackpixel")
    x2 = cv2.getTrackbarPos("X2", "Trackpixel")
    y1 = cv2.getTrackbarPos("Y1", "Trackpixel")
    y2 = cv2.getTrackbarPos("Y2", "Trackpixel")
    xaux = cv2.getTrackbarPos("XAUX", "Trackpixel")
    yaux = cv2.getTrackbarPos("XAUX", "Trackpixel")
    x2 = x2 +  100
    y2 = y2 +  100
    lower_red = np.array([l_h, l_s, l_v])
    upper_red = np.array([u_h, u_s, u_v])
    battlecropped_image = screenshot[x1:x2, y1:y2]
    # cv2.imshow('battlecropped_image', battlecropped_image)
    battlehsv = cv2.cvtColor(battlecropped_image, cv2.COLOR_BGR2HSV)
    maskr = cv2.inRange(battlehsv, lower_red, upper_red)
    # cv2.imshow('maskr', maskr)
    
    bfilter = cv2.bilateralFilter(maskr,11,17,17)
    edged = cv2.Canny(bfilter, 30, 200)
    # cv2.imshow('edged', edged)

    try:
        contours, hierarchy = cv2.findContours(edged, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        location = None ## adap
        if len(contours) != 0:
            for contour in contours:
                if cv2.contourArea(contour) > 5:
                    x,y,w,h = cv2.boundingRect(contour) 
            (xm,ym) = (np.min(x), np.min(y))
            center = (xm,ym)
            print(clock()%1)
            if(clock()%1 < 0.5): 
                pyautogui.moveTo(y1+xm+xaux,ym+x1+yaux)
                pyautogui.click(button='right')
    except:
        pass


    # vê se tem pixel
    # battlepixels = cv2.countNonZero(maskr)
    # print(battlepixels)


    if cv2.waitKey(1) == ord('q'):
        cv2.destroyAllWindows()
        break

print('Done.')