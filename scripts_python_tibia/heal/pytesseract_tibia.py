import cv2
from matplotlib import pyplot as plt
import numpy as np
import imutils
from time import time , clock
# import pytesseract
import os
# import easyocr
from windowcapture_tibia import WindowCapture
import pyautogui
import win32gui, win32ui, win32con, win32api


# pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

os.chdir(os.path.dirname(os.path.abspath(__file__)))
window_name = 'Tibia - Mago Bolahikhjkbasgk'
hwnd = win32gui.FindWindow(None, window_name)
win = win32ui.CreateWindowFromHandle(hwnd)
wincap = WindowCapture(window_name)

lower = np.array([104,150,20])
upper = np.array([126,255,255])
hplower = np.array([0, 0, 255])
hpupper = np.array([180, 255, 255])
loop_time = time()

lower_red = np.array([0,0,188])
upper_red = np.array([0,255,255])


while(True):
    screenshot = wincap.get_screenshot()

    # identifica quadrado
    battlecropped_image = screenshot[441:465, 1740:1770]
    # cv2.imshow('battlecropped_image', battlecropped_image)
    battlehsv = cv2.cvtColor(battlecropped_image, cv2.COLOR_BGR2HSV)
    maskr = cv2.inRange(battlehsv, lower_red, upper_red)
    # cv2.imshow('maskr', maskr)
    battlepixels = cv2.countNonZero(maskr)
    # print(battlepixels)

    mcropped_image = screenshot[8:16, 870:1300]
    hpcropped_image = screenshot[127:128, 1760:1860]
    hphsv = cv2.cvtColor(hpcropped_image, cv2.COLOR_BGR2HSV)
    mhsv = cv2.cvtColor(mcropped_image, cv2.COLOR_BGR2HSV)
    hpmask = cv2.inRange(hphsv, hplower,hpupper)
    bmask = cv2.inRange(mhsv, lower,upper)
    hppixels = cv2.countNonZero(hpmask)
    manapixels = cv2.countNonZero(bmask)
    print(hppixels)
    if hppixels <= 50 and manapixels <= 0:
        win32api.SendMessage(hwnd, win32con.WM_KEYDOWN, 0x75, 0)
        win32api.SendMessage(hwnd, win32con.WM_KEYUP, 0x75, 0)
        # pyautogui.press('6')


    if hppixels <= 80:
        win32api.SendMessage(hwnd, win32con.WM_KEYDOWN, 0x72, 0)
        win32api.SendMessage(hwnd, win32con.WM_KEYUP, 0x72, 0)
        # pyautogui.press('3')

    if manapixels <= 0:
        win32api.SendMessage(hwnd, win32con.WM_KEYDOWN, 0x74, 0)
        win32api.SendMessage(hwnd, win32con.WM_KEYUP, 0x74, 0)
                # pyautogui.press('5')

    if battlepixels > 10 and battlepixels < 70:
        win32api.SendMessage(hwnd, win32con.WM_KEYDOWN, 0x7B, 0)
        win32api.SendMessage(hwnd, win32con.WM_KEYUP, 0x7B, 0)
        win32api.SendMessage(hwnd, win32con.WM_KEYDOWN, 0x71, 0)
        win32api.SendMessage(hwnd, win32con.WM_KEYUP, 0x71, 0)

        # pyautogui.press('space')
        # pyautogui.press('F2')
    if battlepixels > 70  and hppixels > 10:
        if(clock()%3 < 1):  
            win32api.SendMessage(hwnd, win32con.WM_KEYDOWN, 0x70, 0)
            win32api.SendMessage(hwnd, win32con.WM_KEYUP, 0x70, 0)
        # pyautogui.press('F1')
    if(clock()%60 < 1):
        win32api.SendMessage(hwnd, win32con.WM_KEYDOWN, 0x79, 0)
        win32api.SendMessage(hwnd, win32con.WM_KEYUP, 0x79, 0)  
    
    # cv2.imshow('mcropped_image', mcropped_image)
    # cv2.imshow('hpcropped_image', hpcropped_image)
    # print('FPS {}'.format(1 / (time() - loop_time)))
    # print (loop_time)

    key = cv2.waitKey(1)  
    if key == 27:
        break      
exit()
cv2.destroyAllWindows()