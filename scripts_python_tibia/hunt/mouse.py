import time
import pyautogui
while True:
    i = 0
    while i < 20:
        pyautogui.press('2')
        pyautogui.press('3')
        pyautogui.press('4')
        time.sleep(10)
        # pyautogui.press('4')
        # pyautogui.press(']')
        # time.sleep(1)
        # pyautogui.press('9')
        # time.sleep(1)
        i = i+1
    pyautogui.keyDown('ctrl')
    pyautogui.press('left')
    pyautogui.keyUp('ctrl')
    pyautogui.keyDown('ctrl')
    pyautogui.press('up')
    pyautogui.keyUp('ctrl')
#pyautogui.moveTo(864,841)
#pyautogui.click(button='left')