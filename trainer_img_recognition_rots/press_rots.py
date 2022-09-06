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
window_name = 'Return Of The Saiyans'
hwnd = win32gui.FindWindow(None, window_name)
win = win32ui.CreateWindowFromHandle(hwnd)
wincap = WindowCapture(window_name)

hplower = np.array([0, 67, 77])
hpupper = np.array([15, 255, 255])
loop_time = time()


while(True):    
    screenshot = wincap.get_screenshot()
    # win32api.SendMessage(hwnd, win32con.WM_KEYDOWN, 0x72, 0)
    win32api.SendMessage(hwnd, win32con.WM_KEYDOWN, 0x71, 0)
    win32api.SendMessage(hwnd, win32con.WM_KEYDOWN, 0x70, 0)
    # win32api.SendMessage(hwnd, win32con.WM_KEYDOWN, 0x20, 0)
    # win32api.SendMessage(hwnd, win32con.WM_KEYUP, 0x72, 0)
    win32api.SendMessage(hwnd, win32con.WM_KEYUP, 0x71, 0)
    win32api.SendMessage(hwnd, win32con.WM_KEYUP, 0x70, 0)
    # win32api.SendMessage(hwnd, win32con.WM_KEYUP, 0x20, 0)
    hpcropped_image = screenshot[34:142, 69:180]
    hphsv = cv2.cvtColor(hpcropped_image, cv2.COLOR_BGR2HSV)
    hpmask = cv2.inRange(hphsv, hplower,hpupper)
    cv2.imshow('hpmask', hpmask)
    hppixels = cv2.countNonZero(hpmask)

    if hppixels <= 1400:
        win32api.SendMessage(hwnd, win32con.WM_KEYDOWN, 0x72, 0)
        win32api.SendMessage(hwnd, win32con.WM_KEYUP, 0x72, 0)
    if hppixels <= 800:
        win32api.SendMessage(hwnd, win32con.WM_KEYDOWN, 0x73, 0)
        win32api.SendMessage(hwnd, win32con.WM_KEYUP, 0x73, 0)
 
    if(clock()%60 < 1):
        win32api.SendMessage(hwnd, win32con.WM_KEYDOWN, 0x7A, 0)
        win32api.SendMessage(hwnd, win32con.WM_KEYUP, 0x7A, 0)  

    key = cv2.waitKey(1)  
    if key == 27:
        break      
exit()
cv2.destroyAllWindows() 