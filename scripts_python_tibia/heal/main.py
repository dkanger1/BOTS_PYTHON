import cv2 as cv
import numpy as np
import os
from time import time
import pyautogui

os.chdir(os.path.dirname(os.path.abspath(__file__)))


while(True):
    screenshot = pyautogui.screenshot()
    screenshot = np.array(screenshot)

    cv.imshow('Vision', screenshot)

    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break

print('Done')