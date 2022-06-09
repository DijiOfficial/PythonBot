from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

def sleep(a, b):
    sec = round(random.uniform(a,b),4)
    time.sleep(sec)

def clickOnDofus():
    if pyautogui.locateOnScreen("dofusicon.PNG", confidence=0.8) != None:
        x, y = locateCenterOnScreen("dofusicon.PNG", region=(440,1030,760,50), confidence=0.8)
        click(x, y)
    else:
        print("Can't find dofus icon")
        time.sleep(0.5)   

def clickOnZaap(i=0): #can always take a screenshot to see wht happens
    i+=1
    sleep(0.4,0.6)
    if i > 25:
        goToBrakPen()
        raise Exception("can't click on zaap")
    r,g,b = pyautogui.pixel(740, 145)
    if (r in range(79,86) and g in range(105,125) and b in range(90,111)):
        sleep(0.7,1)
        click(740, 145)
    else:
        clickOnZaap(i)

def clickOnZaapi(i=0):
    i+=1
    sleep(0.4,0.6)
    if i == 15:
        clickOnZaapi(i)
    elif i > 25:
        goToBrakPen()
        raise Exception("can't click on zaap")
    r,g,b = pyautogui.pixel(1162, 73)
    if (r == 184 and g == 205 and b == 12) or (r == 177 and g == 204 and b == 12):
        sleep(0.7,1)
        click(1162, 73)
    else:
        clickOnZaapi(i)

def goToBrak():
    sleep(0.9,1.1)
    keyboard.write("brakmar")
    sleep(0.3,0.5)
    keyboard.press_and_release('enter')
    sleep(0.9,1.1)

def tpToPen(i=0):
    i+=1
    sleep(0.4,0.6)
    if i > 25:
        goToBrakPen()
        raise Exception("can't click on zaap")
    if pyautogui.locateOnScreen("teleportbtn.PNG", region=(825,745,265,55), confidence=0.8) != None:
        x, y = locateCenterOnScreen("teleportbtn.PNG", region=(825,725,265,90), confidence=0.8)
        click(1070, 200)
        sleep(0.2,0.4)
        click(820, 320)
        sleep(0.2,0.4)
        click(960, 765)
    else:
        print("fix zaapi window not in right place cunt")
        tpToPen(i)

def clickOnPen(j=0):
    sleep(0.4,0.6)
    r,g,b = pixel(877,498)
    j+=1
    i = 0
    if j >= 10:
        raise Exception("can't click on zaap")
    while True:
        i+=1
        sleep(0.4,0.6)
        click(877, 498)
        sleep(0.2,0.3)
        pyautogui.moveTo(500,500)
        sleep(0.8,1)
        if pyautogui.locateOnScreen("enclos.PNG", region=(490,525,315,70), confidence=0.8) != None or pyautogui.locateOnScreen("enclos2.0.PNG", region=(490,525,315,70), confidence=0.8) != None:
            return
        if i == 5:
            r = pixel(660,420)
            g = pixel(572,356)
            b = pixel(430,500)
            print("can't click on pen")
            if (r[0] == 66 and r[1] == 81 and r[2] == 78) or (g[0] == 141 and g[1] == 120 and g[2] == 49) or (b[0] == 255 and b[1] == 171 and b[2] == 49):
                clickOnPen(j)
            else:
                goToBrakPen()
                raise Exception("can't click on zaap")
                
def pressEsc():
    keyboard.press_and_release('esc')
    sleep(0.9,1.1)
    if pyautogui.locateOnScreen("optionsbtn.PNG", region=(785,385,345,50), confidence=0.8) != None:
        keyboard.press_and_release('esc')

def goToBrakPen():
    sleep(0.2,0.3)
    clickOnDofus()
    sleep(0.4,0.5)
    pressEsc()
    sleep(0.4,0.5)
    keyboard.press_and_release('h')
    try:
        clickOnZaap()
    except:
        return
    goToBrak()
    try:
        clickOnZaapi()
    except:
        return
    sleep(5,5.2)
    try:
        tpToPen()
    except:
        return
    try:
        clickOnPen()
    except:
        return
    print("success")

def test2(j,i=0):
    sleep(1,2)
    print("test2")
    i+=1
    if i > 5 and j < 3:
        test(j)
    if i == 6:
        print("do something")
    else:
        test2(j,i)

def test(j=0):
    j+=1
    sleep(1,2)
    test2(j)
    print("gud")