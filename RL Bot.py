import pyautogui
import time 

##get to main menu on RL (1920x1080) 

time.sleep(2)
##click garage
pyautogui.moveTo(64,676)
pyautogui.click()

time.sleep(2)
##click manage inv
pyautogui.moveTo(64,776)
pyautogui.click()

time.sleep(1)
##select reward item tab on top
pyautogui.moveTo(275,100)
pyautogui.click()

time.sleep(1)
##select reward
pyautogui.moveTo(150,272)
pyautogui.click()
for i in range(55):
    time.sleep(1)
    ##open reward
    pyautogui.moveTo(95,925)
    pyautogui.click()

    time.sleep(1)
    ##confrim open
    pyautogui.moveTo(870,643)
    pyautogui.click()

    time.sleep(8)
    ##click ok
    pyautogui.moveTo(1054,1012)
    pyautogui.click()