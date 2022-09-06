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

while True:
    win32api.SendMessage(hwnd, win32con.WM_KEYDOWN, 0x70, 0)
    win32api.SendMessage(hwnd, win32con.WM_KEYDOWN, 0x71, 0)    
    win32api.SendMessage(hwnd, win32con.WM_KEYDOWN, 0x72, 0)    
    time.sleep(0.2)
    # pyautogui.press('a')
    # pyautogui.press('d')
    # pyautogui.press('w')
    # pyautogui.press('s')
    # pyautogui.press('right')
    # pyautogui.press('f2')
    # pyautogui.press('up')