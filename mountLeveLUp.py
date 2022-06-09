from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con
from gotobrak import clickOnPen, sleep, click, pressEsc, clickOnZaapi, tpToPen
from mountTrainer import waitForMount, goToThirdTab, clickToMove



def clickOnTraining(i=0):
    time.sleep(0.5)
    click(580,145)
    sleep(0.2,0.3)
    test = False
    i+=1
    if i > 5:
        return test
    if pyautogui.locateOnScreen("mountToTrain.png", region=(440,110,300,285), confidence=0.8) == None:
        clickOnTraining(i)
    else:
        x, y = locateCenterOnScreen("mountToTrain.png", region=(440,110,300,285), confidence=0.8)
        test = True
        click(x, y)
    return test

def transferAllToInventory():
    sleep(0.2,0.3)
    click(754,137)
    sleep(0.4,0.6)
    click(921,175)

def equipMount():
    click(1334,391)
    waitForMount()
    keyboard.press_and_release('"')

def goToSecondBar():
    sleep(0.3,0.4)
    r,g,b = pyautogui.pixel(1251,993)
    if (r == 240 and g == 29 and b == 5) or (r == 242 and g == 26 and b == 2):
        return
    goToThirdTab()
    sleep(0.2,0.3)
    pyautogui.moveTo(1276,943)
    sleep(0.2,0.3)
    click(1276,943)

def clickOnFight(i=0):
    sleep(0.2,0.3)
    i+=1
    if i > 20:
        return False
    x = pyautogui.locateCenterOnScreen("mobinfo.png", region=(445,155,990,560), confidence=0.3)   
    if x:
        click(x[0],x[1]+125)
        sleep(0.3,0.5)
        click(367,153)
    else:
        clickOnFight(i)
    return True

def checkFight():
    sleep(0.2,0.3)
    if pixel(1472,959) != (206, 240, 0) or pixel(1547,959) != (208, 241, 0):
        return False
    else:
        print(pixel(1472,959))
        return True

def startFight(i=0):
    sleep(0.2,0.3)
    i+=1
    if i > 20:
        return False
    keyboard.press("z")
    check = clickOnFight()
    keyboard.release("z")
    sleep(1.8,2)
    check2 = checkFight()

    if not check or not check2:
        startFight(i)
    return True

def tpAndFight(i=0):
    goToSecondBar()
    sleep(0.2,0.3)
    i+=1
    if i > 25:
        return False
    keyboard.press_and_release("é") 
    gud = startFight()
    if not gud:
        tpAndFight(i)
    return True

def waitForStart(i=0):
    sleep(0.2,0.3)
    i+=1
    if i > 20:
        return
    if pixel(849,634) == (221, 34, 0) or pixel(1024,637) == (221, 34, 0):
        waitForStart(i)

def puissance():
    sleep(0.2,0.3)
    keyboard.press_and_release('"')
    sleep(0.2,0.3)

def epeeIop():
    sleep(0.2,0.3)
    keyboard.press_and_release("è")
    sleep(0.2,0.3)

def start():
    sleep(0.2,0.3)
    keyboard.press_and_release("q")
    sleep(0.2,0.3)

def epeeCeleste():
    sleep(0.2,0.3)
    keyboard.press_and_release("§")
    sleep(0.2,0.3)  

def double(x,y):
    sleep(0.2,0.3)
    click(x,y)
    sleep(0.05,0.08)
    click(x,y)
    sleep(0.2,0.3)

def pos3():
    x,y=0.2,0.3
    start()
    sleep(0.7,0.9)
    waitForStart()
    double(851,590)
    waitForMe(851,590)
    puissance()
    double(851,590)
    epeeIop()
    double(894,569)
    epeeIop()
    double(894,569)
    epeeCeleste()
    double(894,569)

def pos2():
    x,y=0.5,0.6
    start()
    sleep(0.7,0.9)
    waitForStart()
    sleep(x,y)
    puissance()
    sleep(x,y)
    double(811,480)
    epeeIop()
    click(854,502)
    sleep(x,y)
    epeeIop()
    click(854,502)
    sleep(x,y)
    epeeCeleste()
    double(854,502)
    sleep(x,y)
    epeeCeleste()
    double(854,502)

def waitForMe(x=1068,y=481):
    sleep(0.2,0.3)
    x = pixel(x, y)
    print(x)
    if x == (138, 93, 40) or x == (83, 96, 24) or x == (0, 102, 0):
        waitForMe()
##def copywaitForMe(i=0):
##    sleep(0.2,0.3)
##    i+=1
##    if i>25:
##        return
##    x = pixel(1081,482)
##    if x == (138, 93, 40) or x == (83, 96, 24) or x == (0, 102, 0):
##        waitForMe(i)
        
def waitForMe2():
    sleep(0.2,0.3)
    x = pixel(1111,504)
    if x == (148, 103, 50) or x == (138, 93, 40) or x == (83, 96, 24) or x == (0, 102, 0):
        waitForMe2()
    print(x)
     
def pos1a(): #solwed down x,y
    x,y=0.5,0.6
    start()
    sleep(0.7,0.9)
    waitForStart()
    sleep(x,y)
    puissance()
    double(1022,457)
    sleep(x,y)
    epeeIop()
    click(980,483)
    sleep(x,y)
    epeeIop()
    click(980,483)
    double(1068,481)
    # double(1068,481)
    sleep(0.05,0.1)
    moveTo(1000,500)
    sleep(0.5,0.8)
    waitForMe(1068,481)
    epeeCeleste()
    double(1023,505)
    
def pos1b(): #can verify which mob still alive
    x,y=0.3,0.4
    start()
    sleep(0.7,0.9)
    waitForStart()
    sleep(x,y)
    puissance()
    double(1068,481)
    sleep(x,y)
    epeeIop()
    click(1023,504)
    sleep(x,y)
    epeeIop()
    click(1023,504)
    sleep(x,y)
    epeeCeleste()
    double(1023,504)

def pos1c():
    x,y=0.3,0.4
    start()
    sleep(0.7,0.9)
    waitForStart()
    sleep(0.2,0.3)
    puissance()
    double(1068,481)
    sleep(x,y)
    epeeCeleste()
    click(1025,502)
    sleep(0.5,0.6)
    double(1111,504)
    sleep(0.5,0.8)
    waitForMe2()
    epeeIop()
    double(1068,524)
    epeeIop()
    double(1068,524)

def checkFirstPos():
    sleep(0.2,0.3)
    if pixel(1066,612) == (221, 34, 0):
        click(1066,612)
    
def fight(): ##add more checks and restart fight()
    sleep(0.5,0.6)
    if pixel(811,525) != (97, 75, 93):
        print(pixel(811,525))
##        sleep(0.2,0.3)
        if pixel(936,549) != (104, 82, 100) and pixel(1114,549) == (104, 82, 100):
            print(pixel(936,549),pixel(1114,549))
##            sleep(0.2,0.3)
            if pixel(977,612) != (97, 75, 93):
                print(pixel(977,612))
                print("pos3")
                checkFirstPos()
                sleep(0.2,0.3)
                click(806,612)
                pos3()
            elif pixel(937,459) != (104, 82, 100):
                print(pixel(937,459))
                print("pos2")
                checkFirstPos()
                sleep(0.2,0.3)
                click(811,480)
                pos2()
            else:
                fight()
        else:
            fight()
    elif pixel(936,549) == (104, 82, 100):
        sleep(0.2,0.3)
        if pixel(897,525) != (97, 75, 93):
            print(pixel(897,525))
            print("pos1a")
            checkFirstPos()
            sleep(0.2,0.3)
            click(1022,457)
            pos1a()
        elif pixel(897,570) != (97, 75, 93):
            print(pixel(897,570))
            print("pos1b")
            checkFirstPos()
            sleep(0.2,0.3)
            click(1068,481)
            pos1b()
        elif pixel(980,568) != (97, 75, 93):
            print(pixel(980,568))
            print("pos1c")
            checkFirstPos()
            sleep(0.2,0.3)
            click(1068,481)
            pos1c()
        else:
            print("error placement unknown")
    else:
        print(pixel(936,549))
        fight()
        
def checkEmpty():
    time.sleep(1)
    if pyautogui.locateOnScreen("empty3.0.png", region=(1280,800,80,80), confidence=0.9) != None:
        return True
    else:
        return False

def waitForEnd():
    sleep(0.2,0.3)
    if pixel(1040,181) != (110, 132, 35):
        waitForEnd()

def mountMount(j=0):
    sleep(0.2,0.3)
    j+=1
    if j == 1:
        keyboard.press_and_release("e")
    sleep(0.5,0.6)
    i=0
    keyboard.press_and_release("e")
    while i < 15:
        sleep(0.2,0.3)
        i+=1
        if pixel(963,763) == (192, 233, 0):
            break
    if i >= 15:
        mountMount(j)
    sleep(0.2,0.3)
    click(963,763)

def checkCreatureAndLocked():
    sleep(0.2,0.3)
    if pixel(1486,903) == (88, 88, 88):
        click(1486,903)
    sleep(0.2,0.3)
    if pixel(1474,1005) == (173, 173, 173):
        click(1474,1005)
        
def train():
    sleep(0.4,0.5)
    equipMount()
    sleep(0.2,0.3)
    pressEsc()
    sleep(0.2,0.3)
    moveTo(500,500)
    mountMount()
    sleep(0.2,0.3)
    pressEsc()
    check = tpAndFight()
    if not check:
        return
    checkCreatureAndLocked()
    fight()
    waitForEnd()
    sleep(0.4,0.5)
    pressEsc()
    sleep(0.2,0.3)
    keyboard.press_and_release("&")
    sleep(0.4,0.5)
    clickOnZaapi()
    tpToPen()
    clickOnPen()
    check = checkEmpty()
    if not check:
        train()
    
def moveMount(i=0):
    sleep(0.2,0.3)
    i+=1
    if i > 10:
        return False
    mount = pyautogui.locateCenterOnScreen("mainmount.png", region=(0,0,1830,365), confidence=0.8)
    if mount:
        sleep(0.2,0.3)
        clickToMove(mount[0],mount[1],(1071,121))
    else:
        moveMount(i)
    return True

def prep():
    sleep(0.2,0.3)
    pressEsc()
    goToThirdTab()
    sleep(0.2,0.3)
    keyboard.press_and_release("é")
    sleep(0.2,0.3)
    keyboard.press_and_release("e")
    mountIsFound = moveMount()
    if not mountIsFound:
        return
    sleep(0.2,0.3)
    click(1200,290)
    sleep(0.2,0.3)
    click(1115,330)
    sleep(0.2,0.3)
    click(1330,328)
    sleep(0.2,0.3)
    pressEsc()
    sleep(0.2,0.3)
    keyboard.press_and_release("à")

def fastGraph():
    sleep(0.2,0.3)
    keyboard.press_and_release("esc")
    sleep(1.2,1.3)
    if pyautogui.locateOnScreen("optionsbtn.PNG", region=(785,385,345,50), confidence=0.8) != None:
        click(962,410)
    else:
        fastGraph()
    while True:
        sleep(0.2,0.3)
        if pyautogui.locateOnScreen("options.PNG", region=(860,65,215,100), confidence=0.8) != None:
            break
    click(1282,450)
    sleep(0.4,0.5)
    click(1273,471)
    sleep(0.4,0.5)
    click(1272,500)
    sleep(0.4,0.5)
    click(1273,527)
    sleep(0.4,0.5)
    click(1448,436)
    sleep(0.4,0.5)
    click(1283,406)
    sleep(0.4,0.5)
    click(1277,435)
    sleep(0.4,0.5)
    pressEsc()
    
def mainLvlUp():
    sleep(0.2,0.3)
    pressEsc()
    prep()
    fastGraph()
    clickOnPen()
    trainingIsFound = clickOnTraining()
    if not trainingIsFound:
        return
    sleep(0.2,0.3)
    transferAllToInventory()
    sleep(0.2,0.3)
    train()
    #unprep put back mount grapics etc...
