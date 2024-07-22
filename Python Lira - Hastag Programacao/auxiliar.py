import pyautogui
import time

for x in range(0,20):
    time.sleep(4)
    #print(pyautogui.position())

    pyautogui.click(x=437, y=716)

    time.sleep(4)
    #print(pyautogui.position())

    pyautogui.click(x=559, y=331)
    time.sleep(4)
    pyautogui.press("f5")