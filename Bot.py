from pyautogui import *
import pyautogui
import pyautogui as pag
import random
import time
import keyboard
import numpy as np
import win32api, win32con
import pyscreeze

apsc    = 132
chemlab = 247
chem = 484
phys158 = 593

yes     = 0
no      = 1

# WRITE WHAT CLASS BELOW VV
# ----------------------------------------------------------------------
# apsc
# chemlab
# chem
# phys158


lect      = apsc
tabOpen   = no
classOpen = no



# ----------------------------------------------------------------------

if lect == 132:
    xB = np.random.randint(605, 635)
elif lect == 247:
    xB = np.random.randint(605, 635)
elif lect == 484:
    xB = np.random.randint(605, 635)
elif lect == 593:
    xB = np.random.randint(605, 635)
else: 
    xB = np.random.randint(605, 635)


def click():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(np.random.uniform(0.02,0.06))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

from pyclick import HumanClicker
hc = HumanClicker()

time.sleep(1.5)

if tabOpen == 1:
    pag.moveTo(871,1058,0)
    click()
    time.sleep(0.1)
    click()

    time.sleep(2)
    pag.moveTo(900,500,0)
    click()
    time.sleep(0.2)
    pyautogui.press('f11')

    time.sleep(0.2)
    pag.moveTo(1861,15,0)
    click()
    time.sleep(0.5)
    pag.moveTo(1635,380,0)
    click()

    time.sleep(2)

    pag.moveTo(520,375,0)
    click()

    time.sleep(0.2)
    pag.moveTo(660,425,0)
    time.sleep(0.2)
    click()
    time.sleep(0.2)
    click()

    time.sleep(0.2)
    pag.moveTo(532,500,0)
    click()

    time.sleep(12)

    pag.moveTo(540,277,0)
    click()

    time.sleep(3)
    pag.moveTo(151,325,0)
    click()

    time.sleep(2)
    pag.moveTo(860,160,0)
    click()

    time.sleep(1.5)
    pag.moveTo(1264,538,0)
    click()

    time.sleep(1.5)
    pag.moveTo(621,310,0)
    click()

    time.sleep(0.2)
    pag.moveTo(755,366,0)
    click()
    time.sleep(0.2)
    click()
    time.sleep(0.2)
    click()

    time.sleep(0.2)
    pag.moveTo(956,533,0)
    click()

    time.sleep(4)

    hc.move((660,lect), np.random.uniform(0.8,2.2))
    click()

time.sleep(1)

if classOpen == 1:
    while True:
        if pyautogui.pixel(1231, 161)[1] == 121:
            time.sleep(.5)
            hc.move((1263, 161), np.random.uniform(0.8,2.2))
            time.sleep(.5)
            click()
            time.sleep(1)
            break
        time.sleep(0.5)

hc.move((np.random.randint(200, 1800), np.random.randint(100, 900)), np.random.uniform(0.5, 3))

time.sleep(2)

hc.move((np.random.randint(200, 1800), np.random.randint(100, 900)), np.random.uniform(0.5, 3))

time.sleep(1)

while keyboard.is_pressed('q') == False:
    time.sleep(np.random.uniform(1,5))
    try: 
        if pyautogui.locateOnScreen('iclicker_Fav.png', grayscale=True, confidence=0.8) != None:
            x = np.random.uniform(0,2)
            time.sleep(np.random.uniform(1, 3))
            if 0 <= x < 0.5:
                hc.move((np.random.randint(200, 1800), np.random.randint(100, 900)), np.random.uniform(0.5, 3))
    except pyautogui.ImageNotFoundException: 
        x = np.random.uniform(0,3.3)
        if 0 <= x < 1:
            time.sleep(np.random.uniform(2,5))
            hc.move((673, xB), np.random.uniform(0.2, 2.1))
            time.sleep(np.random.uniform(0.5,2))
            click()
            time.sleep(np.random.uniform(0.1,2))
            hc.move((np.random.randint(200, 1800), np.random.randint(100, 900)), np.random.uniform(0.3,2))
        elif 1 <= x < 2:
            time.sleep(np.random.uniform(1,4))
            hc.move((815, xB), np.random.uniform(0.3,1))
            time.sleep(np.random.uniform(0.1,1))
            click()
            time.sleep(np.random.uniform(0.1,2))
            hc.move((np.random.randint(200, 1800), np.random.randint(100, 900)), np.random.uniform(0.3,2))
        elif 2 <= x < 3:
            time.sleep(np.random.uniform(2,4))
            hc.move((959, xB), np.random.uniform(0.2,2.2))
            time.sleep(np.random.uniform(0.5,3))
            click()
            time.sleep(np.random.uniform(0.1,2))
            hc.move((np.random.randint(200, 1800), np.random.randint(100, 900)), np.random.uniform(0.3,3))
        else:
            time.sleep(np.random.uniform(1,5))
            hc.move((1105, xB), np.random.uniform(0.3,2.5))
            time.sleep(np.random.uniform(0.3,1))
            click()
            time.sleep(np.random.uniform(0.1,2))
            hc.move((np.random.randint(200, 1800), np.random.randint(100, 900)), np.random.uniform(0.3,2))
        time.sleep(np.random.uniform(0,0))
    time.sleep(0.1)

