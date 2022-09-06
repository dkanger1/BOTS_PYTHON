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
map_count=0
os.chdir(os.path.dirname(os.path.abspath(__file__)))
window_name = 'Tibia - Carangueijo na Desova'
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
def heal_func(hppixels,manapixels,hwnd):
    # print(manapixels)
    print(hppixels)
    if hppixels <= 65 and (clock()%1 < 0.3):
        win32api.SendMessage(hwnd, win32con.WM_KEYDOWN, 0x71, 0)  ##F2
        win32api.SendMessage(hwnd, win32con.WM_KEYUP, 0x71, 0)
    if hppixels <= 79 and (clock()%1 < 0.3):
        win32api.SendMessage(hwnd, win32con.WM_KEYDOWN, 0x78, 0)#F3
        win32api.SendMessage(hwnd, win32con.WM_KEYUP, 0x78, 0)
    if manapixels <= 10:
        win32api.SendMessage(hwnd, win32con.WM_KEYDOWN, 0x72, 0)#F3
        win32api.SendMessage(hwnd, win32con.WM_KEYUP, 0x72, 0)
        # pyautogui.press('5')
    if hppixels <= 50 and manapixels <= 5:
        win32api.SendMessage(hwnd, win32con.WM_KEYDOWN, 0x75, 0)
        win32api.SendMessage(hwnd, win32con.WM_KEYUP, 0x75, 0)
        # pyautogui.press('6')
    # if hppixels <= 15:
    #     pyautogui.press('v')
    #     pyautogui.press('c')


def battle_func(battlepixels,manapixels,hwnd):

    if battlepixels > 10 and battlepixels < 70:
        # pyautogui.press('space')
        win32api.SendMessage(hwnd, win32con.WM_KEYDOWN, 0x7B, 0)
        win32api.SendMessage(hwnd, win32con.WM_KEYUP, 0x7B, 0)

    # pyautogui.press('space')
    # pyautogui.press('F2')
    if battlepixels > 70  and manapixels > 10:
        if(clock()%4 < 1):  
            win32api.SendMessage(hwnd, win32con.WM_KEYDOWN, 0x75, 0)
            win32api.SendMessage(hwnd, win32con.WM_KEYUP, 0x75, 0)
        if(clock()%2 < 1):  
            win32api.SendMessage(hwnd, win32con.WM_KEYDOWN, 0x70, 0)
            win32api.SendMessage(hwnd, win32con.WM_KEYUP, 0x70, 0)
        # pyautogui.press('F1')
    
    if(clock()%15 < 1):
        win32api.SendMessage(hwnd, win32con.WM_KEYDOWN, 0x73, 0)
        win32api.SendMessage(hwnd, win32con.WM_KEYUP, 0x73, 0)  
    # if(clock()%60 < 1):
    #     win32api.SendMessage(hwnd, win32con.WM_KEYDOWN, 0x7A, 0)
    #     win32api.SendMessage(hwnd, win32con.WM_KEYUP, 0x7A, 0)




def cavebot(map_count):
    win32api.SendMessage(hwnd, win32con.WM_KEYDOWN, 0x7A, 0)
    win32api.SendMessage(hwnd, win32con.WM_KEYUP, 0x7A, 0)

    if(map_count == 0):
        pyautogui.click(pyautogui.locateOnScreen('heal/imgs/icon1.png',region=(1741,35,135,105), grayscale = True, confidence = 0.8))
        return
    if(map_count == 1):
        pyautogui.click(pyautogui.locateOnScreen('heal/imgs/icon2.png',region=(1741,35,135,105), confidence = 0.6))
        return
    if(map_count ==2):
        pyautogui.click(pyautogui.locateOnScreen('heal/imgs/icon3.png',region=(1741,35,135,105), confidence = 0.6))
        return
    if(map_count == 3):
        pyautogui.click(pyautogui.locateOnScreen('heal/imgs/icon4.png',region=(1741,35,135,105), confidence = 0.6))
        return
    if(map_count == 4):
        pyautogui.click(pyautogui.locateOnScreen('heal/imgs/icon5.png',region=(1741,35,135,105), confidence = 0.6))
        return
    # if(map_count == 5):
    #     pyautogui.click(pyautogui.locateOnScreen('heal/imgs/icon8.png',region=(1741,35,135,105), confidence = 0.6))
    #     return
    # if(map_count == 6):
    #     pyautogui.click(pyautogui.locateOnScreen('heal/imgs/icon9.png',region=(1741,35,135,105), confidence = 0.6))
    #     return
    # if(map_count == 7):
    #     pyautogui.click(pyautogui.locateOnScreen('heal/imgs/icon10.png',region=(1741,35,135,105), confidence = 0.6))
    #     return

while(True):
    screenshot = wincap.get_screenshot()
    mcropped_image = screenshot[22:23, 1763:1845]
    hpcropped_image = screenshot[12:13, 1763:1845]
    # cv2.imshow('MANA', mcropped_image)
    # cv2.imshow('LIFE', hpcropped_image)
    hphsv = cv2.cvtColor(hpcropped_image, cv2.COLOR_BGR2HSV)
    mhsv = cv2.cvtColor(mcropped_image, cv2.COLOR_BGR2HSV)
    hpmask = cv2.inRange(hphsv, hplower,hpupper)
    bmask = cv2.inRange(mhsv, lower,upper)
    hppixels = cv2.countNonZero(hpmask)
    manapixels = cv2.countNonZero(bmask)



#########               battle         ##################
    # cv2.imshow('battlecropped_image', battlecropped_image)
    # cv2.imshow('maskr', maskr)
    battlecropped_image = screenshot[441:465, 1740:1770]
    battlehsv = cv2.cvtColor(battlecropped_image, cv2.COLOR_BGR2HSV)
    maskr = cv2.inRange(battlehsv, lower_red, upper_red)
    battlepixels = cv2.countNonZero(maskr)

###############################################################
    heal_func(hppixels,manapixels,hwnd)
    battle_func(battlepixels,manapixels,hwnd)
    if( battlepixels == 0 and hppixels > 50 and clock()%7 < 0.6):
        cavebot(map_count)
        map_count = map_count +1
        print("foi")
        if(map_count == 7):
            map_count = 0
    if(clock()%15 < 1):  
        win32api.SendMessage(hwnd, win32con.WM_KEYDOWN, 0x77, 0)
        win32api.SendMessage(hwnd, win32con.WM_KEYUP, 0x77, 0) 

    key = cv2.waitKey(1)  
    if key == 27:
        break      
exit()
cv2.destroyAllWindows()