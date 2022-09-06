import cv2
from matplotlib import pyplot as plt
import numpy as np
import imutils
from time import time , clock,sleep
# import pytesseract
import os
# import easyocr
from windowcapture_tibia import WindowCapture
import pyautogui
import win32gui, win32ui, win32con, win32api

os.chdir(os.path.dirname(os.path.abspath(__file__)))
window_name = 'Tibia - Cacacor Cocaz'
hwnd = win32gui.FindWindow(None, window_name)
win = win32ui.CreateWindowFromHandle(hwnd)
wincap = WindowCapture(window_name)

while(True):
    win32api.SendMessage(hwnd, win32con.WM_KEYDOWN, 0x70, 0)  ##F1
    win32api.SendMessage(hwnd, win32con.WM_KEYUP, 0x70, 0)
    sleep(1)
    win32api.SendMessage(hwnd, win32con.WM_KEYDOWN, 0x71, 0)  
    win32api.SendMessage(hwnd, win32con.WM_KEYUP, 0x71, 0)
    sleep(1)    
    win32api.SendMessage(hwnd, win32con.WM_KEYDOWN, 0x70, 0)  ##F1
    win32api.SendMessage(hwnd, win32con.WM_KEYUP, 0x70, 0)
    sleep(1)    
    win32api.SendMessage(hwnd, win32con.WM_KEYDOWN, 0x71, 0)  
    win32api.SendMessage(hwnd, win32con.WM_KEYUP, 0x71, 0)
    sleep(1) 