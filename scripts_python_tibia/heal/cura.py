import cv2
import numpy as np
import os
from time import time
from windowcapture_tibia import WindowCapture

def nothing(x):
    pass
os.chdir(os.path.dirname(os.path.abspath(__file__)))

#WindowCapture.list_window_names()
#exit()
# initialize the WindowCapture class
wincap = WindowCapture('Tibia - Paladino Acacinu')

loop_time = time()

cv2.namedWindow("Trackbars")
cv2.createTrackbar("L-H", "Trackbars", 0,180, nothing)
cv2.createTrackbar("L-S", "Trackbars", 0,255, nothing)
cv2.createTrackbar("L-V", "Trackbars", 0,255, nothing)
cv2.createTrackbar("U-H", "Trackbars", 180,180, nothing)
cv2.createTrackbar("U-S", "Trackbars", 255,255, nothing)
cv2.createTrackbar("U-V", "Trackbars", 255,255, nothing)
cv2.createTrackbar("HP", "Trackbars", 0,50, nothing)
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
    hp = cv2.getTrackbarPos("HP", "Trackbars")
    hpp = hp +  435
    lower_red = np.array([l_h, l_s, l_v])
    upper_red = np.array([u_h, u_s, u_v])
    battlecropped_image = screenshot[441:465, 1740:1770]
    cv2.imshow('battlecropped_image', battlecropped_image)
    battlehsv = cv2.cvtColor(battlecropped_image, cv2.COLOR_BGR2HSV)
    maskr = cv2.inRange(battlehsv, lower_red, upper_red)
    cv2.imshow('maskr', maskr)
    battlepixels = cv2.countNonZero(maskr)
    print(battlepixels)


    if cv2.waitKey(1) == ord('q'):
        cv2.destroyAllWindows()
        break

print('Done.')