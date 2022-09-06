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
l_h = 74
l_s =88
l_v = 176
u_h = 180
u_s =255
u_v = 255
x1 = 359
x2 = 631
y1 = 703
y2 = 1176
xaux = 20
yaux = 70
loop_time = time()
count = input("Quantidade de stamina:")
while(True):
    if round(clock()) > int(count):
        break
    print( round(clock()))
    screenshot = wincap.get_screenshot()
    #print('FPS {}'.format(1 / (time() - loop_time)))
    loop_time = time()

    lower_red = np.array([l_h, l_s, l_v])
    upper_red = np.array([u_h, u_s, u_v])
    battlecropped_image = screenshot[x1:x2, y1:y2]
    battlehsv = cv2.cvtColor(battlecropped_image, cv2.COLOR_BGR2HSV)
    maskr = cv2.inRange(battlehsv, lower_red, upper_red)
    
    bfilter = cv2.bilateralFilter(maskr,11,17,17)
    edged = cv2.Canny(bfilter, 30, 200)
    cv2.imshow('edged', edged)

    try:
        contours, hierarchy = cv2.findContours(edged, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        # print(contours)
        location = None ## adap
        if len(contours) != 0:
            for contour in contours:
                if cv2.contourArea(contour) > 5:
                    x,y,w,h = cv2.boundingRect(contour)
            (xm,ym) = (np.min(x), np.min(y))
            center = (xm,ym)
            # print(center)
            # if(clock()%1 < 1): 
            pyautogui.moveTo(y1+xm+xaux,ym+x1+yaux)
            pyautogui.click()
    except:
        pass
    if cv2.waitKey(1) == ord('q'):
        cv2.destroyAllWindows()
        break

print('Done.')