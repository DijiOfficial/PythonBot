from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con
from gotobrak import clickOnPen, sleep, click, pressEsc

def checkEnclos():
    sleep(0.3,0.4)
    if pyautogui.locateOnScreen("enclos.PNG", region=(490,525,315,70), confidence=0.8) == None and pyautogui.locateOnScreen("enclos2.0.PNG", region=(490,525,315,70), confidence=0.8) == None:
        pressEsc()
        clickOnPen()
        return True
    return False

def clickDroit(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN,0,0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP,0,0)

def clickToMove(x,y,pos):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    sleep(0.01,0.03)
    pyautogui.moveTo(pos[0],pos[1])
    sleep(0.01,0.03)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

def goToThirdMount():
    sleep(0.2,0.3)
    click(763,194)
##    sleep(0.4,0.6)
##    click(725,170)
##    sleep(0.2,0.3)
##    click(725,170)
    sleep(0.4,0.5)
    click(590, 205)
##    for i in range(3):
##        sleep(0.2,0.3)
##        keyboard.press_and_release('down')

def transferToInventory():
    sleep(0.2,0.3)
    keyboard.press_and_release("'")

def loopSteril():
    sleep(0.2,0.3)
    if pyautogui.locateOnScreen("sterile.PNG", region=(920,480,130,35), confidence=0.8) != None:
        transferToInventory()
        waitForMount()
    else:
        keyboard.press_and_release("down")
    
def checkSteril():
    isEnd = False
    goToThirdMount()
    while not isEnd:
        loopSteril()
        r,g,b = pyautogui.pixel(764,478)
        if (r != 63 and g != 64 and b != 56):        
            isEnd = True
    for i in range(15):
        loopSteril()

##def closeEsc():
##    sleep(0.4,0.5)
##    keyboard.press_and_release('esc')

def emptyPen():
    sleep(0.2,0.3)
    click(755,605)
    sleep(0.3,0.4)
    click(870,625)
    sleep(0.2,0.3)
    click(590, 570)

def goToThirdTab():
    sleep(0.3,0.4)
    if pyautogui.locateOnScreen("angryicon.png", region=(1090,870,130,130), confidence=0.8) != None:
        return
    for i in range(6):
        sleep(0.2,0.3)
        pyautogui.moveTo(1276,943)
        sleep(0.2,0.3)
        click(1276,943)
    r,g,b = pyautogui.pixel(1250,953)
    if (r ==14 and g == 147 and b == 193):
        for i in range(2):
            sleep(0.2,0.3)
            pyautogui.moveTo(1275,983)
            sleep(0.2,0.3)
            click(1275,983)
    else:
        sleep(0.2,0.3)
        pyautogui.moveTo(1300,953)
        sleep(0.2,0.3)
        click(1300,953)
        goToThirdTab()
    goToThirdTab()

def clearPen():
    pos =[((1024,589),(1073,601)),((938,588),(984,606)),((896,567),(941,580)),((1025,548),(1084,563)),((982,523),(1043,538))]
    for i in pos:
        sleep(0.4,0.5)
        click(i[0][0], i[0][1])
        sleep(0.4,0.5)
        click(i[1][0], i[1][1])

def fillPen():
    pos = [(1025, 548),(938, 588),(982, 523),(896, 567),(1024, 589)]
    keys = ['"',"'","(","§","è"]
    for i in range(5):
        for j in range(5-i):
            sleep(0.4,0.5)
            keyboard.press_and_release(keys[i])
            sleep(0.4,0.5)
            click(pos[j+i][0],pos[j+i][1])

def moveInventory(i,j):
    i+=1
    if (i>15):
        keyboard.press_and_release('i')
        i = 0
        j+=1
    if j > 3:
        if j == 5:
            return
        pressEsc()
        sleep(0.4,0.5)
        pressEsc()
        sleep(0.4,0.5)
        pressEsc()
        sleep(0.4,0.5)
        keyboard.press_and_release('i')
    sleep(0.2,0.3)
    if pyautogui.locateOnScreen("inventory.PNG", region=(360,0,1200,280), confidence=0.8) != None:
        x,y = pyautogui.locateCenterOnScreen("inventory.PNG", region=(360,0,1200,280), confidence=0.8)
        clickToMove(x,y,(1071,121))
    elif pyautogui.locateOnScreen("inventaire.PNG", region=(360,0,1200,280), confidence=0.8) != None:
        x,y = pyautogui.locateCenterOnScreen("inventaire.PNG", region=(360,0,1200,280), confidence=0.8)
        clickToMove(x,y,(1071,121))
    else:
        print("can't find inventory")
        moveInventory(i,j)

def clickOnObj(i):
    sleep(0.2,0.3)
    if i >= 15:
        return
    if pyautogui.locateOnScreen("breedingobj.PNG", region=(1170,180,280,280), confidence=0.8) != None:
        x,y = pyautogui.locateCenterOnScreen("breedingobj.PNG", region=(1170,180,280,280), confidence=0.8)
        click(x,y)
    else:
        print("Can't find objet elevage")
        i+=1
        clickOnObj(i)

def moveObj(obj):
    sleep(0.4,0.5)
    objFound = 0
    bar = [(950,945),(986,945),(1033,945),(1076,945),(1116,945)]
    for i in range(10):
        for j in range(5):
            if(objFound == 5):
                break
            pyautogui.moveTo(1198+(j*59),241+(i*59))
            sleep(0.5,0.6)
            if pyautogui.locateOnScreen("effet.png", region=(735,285,120,165), confidence=0.8) == None:
                return
            elif objFound < 5 and pyautogui.locateOnScreen("{}.png".format(obj), region=(1015,245,125,120), confidence=0.8) != None:
                if pyautogui.locateOnScreen("empty.png", region=(850,380,120,110), confidence=0.8) != None:
                    print("{} at 0".format(obj))
                else:
                    clickToMove(1198+(j*59),241+(i*59),bar[objFound])
                    objFound +=1
##            else:
##                print("{} not found".format(obj))

def clearBar():
    sleep(0.4,0.5)
    bar = [(950,945),(986,945),(1033,945),(1076,945),(1116,945)]
    for i in bar:
        sleep(0.6,0.7)
        clickDroit(i[0],i[1])
        sleep(0.6,0.7)
        if pyautogui.locateOnScreen("retirer.png", region=(920,890,350,40), confidence=0.8) != None:
            click(i[0]+40,i[1]-40)
    
def selectBreedingObj(obj):
    sleep(0.2,0.3)
    keyboard.press_and_release('i')
    inventoryIterate = 0
    moveInventory(inventoryIterate,0)
    sleep(0.2,0.3)
    click(1296, 161)
    sleep(0.2,0.3)
    click(1332,191)
    clickOnObj(0)
    moveObj(obj)
    
def checkLove(isDefault=True, moreInfo=False):
    i = 0
    mounts = 0
    mountFound = False
    needSerenity = False
    isEnd = False
    goToThirdMount()
    waitForMount()
    while not isEnd and i < 300 and mounts < 10 and not needSerenity:
        i+=1
        res1, res2 = loopLove(isDefault)
        if res1 and isDefault:
            needSerenity = True
            mountFound = True
        elif res2:
            if not isDefault:
                mounts+=1
            mountFound = True
        r,g,b = pyautogui.pixel(764,478)
        if (r != 63 or g != 64 or b != 56):
            check = checkEnclos()
            if check:
                checkLove(isDefault,moreInfo)
            isEnd = True
    if i >= 300:
        checkEnclos()
        checkLove(isDefault,moreInfo)
    waitForMount()
    for i in range(15):
        if mounts >= 10 or needSerenity:
            break
        res1, res2 = loopLove(isDefault)
        if res1 and isDefault:
            needSerenity = True
            mountFound = True
        elif res2:
            if not isDefault:
                mounts+=1
            mountFound = True
    if moreInfo:
        return True if mounts >= 10 else False        
    return mountFound, needSerenity

def checkEnergy():
    ##updated version of the checks which removes putting them in the pen just checks if energy is needed  
    i = 0
    ##mountFound = False
    male, female = False, False
    isEnd = False
    goToThirdMount()
    waitForMount()
    while not isEnd and i < 300 and (not male and not female):
        i+=1
        res1, res2 = loopE("other") #reuse function instead of creating new one
        if res1:
            male = True
        elif res2:
            female = True
        r,g,b = pyautogui.pixel(764,478)
        if (r != 63 or g != 64 or b != 56):
            check = checkEnclos()
            if check:
                checkEnergy()
            isEnd = True
    if i >= 300:
        checkEnclos()
        checkEnergy()
    waitForMount()
    for i in range(15):
        if male or female:
            break
        res1, res2 = loopE("other")
        if res1:
            male = True
        elif res2:
            female = True
    return male, female

def checkMaturity(isDefault=True, moreInfo=False):
    i = 0
    mounts = 0
    mountFound = False
    needSerenity = False
    isEnd = False
    goToThirdMount()
    waitForMount()
    while not isEnd and mounts < 10 and i < 300 and not needSerenity:
        i+=1
        res1, res2 = loopMaturity(isDefault)
        if res1 and isDefault:
            needSerenity = True
            mountFound = True
        elif res2:
            if not isDefault:
                mounts+=1
            mountFound = True
        r,g,b = pyautogui.pixel(764,478)
        if (r != 63 or g != 64 or b != 56):
            check = checkEnclos()
            if check:
                checkMaturity(isDefault,moreInfo)
            isEnd = True
    if i >= 300:
        checkEnclos()
        checkMaturity(isDefault,moreInfo)
    waitForMount()
    for i in range(15):
        if mounts >= 10 or needSerenity:
            break
        res1, res2 = loopMaturity(isDefault)
        if res1 and isDefault:
            needSerenity = True
            mountFound = True
        elif res2:
            if not isDefault:
                mounts+=1
            mountFound = True
    if moreInfo:
        return True if mounts >= 10 else False        
    return mountFound, needSerenity

def checkEndurance(isDefault=True, moreInfo=False):
    i = 0
    mounts = 0
    mountFound = False
    needSerenity = False
    isEnd = False
    goToThirdMount()
    waitForMount()
    while not isEnd and i < 300 and mounts < 10 and not needSerenity:
        i+=1
        res1, res2 = loopEndurance(isDefault)
        if res1 and isDefault:
            needSerenity = True
            mountFound = True
        elif res2:
            if not isDefault:
                mounts+=1
            mountFound = True
        r,g,b = pyautogui.pixel(764,478)
        if (r != 63 or g != 64 or b != 56):
            check = checkEnclos()
            if check:
                checkEndurance(isDefault,moreInfo)
            isEnd = True
    if i >= 300:
        checkEnclos()
        checkEndurance(isDefault,moreInfo)
    waitForMount()
    for i in range(15):
        if mounts >= 10 or needSerenity:
            break
        res1, res2 = loopEndurance(isDefault)
        if res1 and isDefault:
            needSerenity = True
            mountFound = True
        elif res2:
            if not isDefault:
                mounts+=1
            mountFound = True
    if moreInfo:
        return True if mounts >= 10 else False        
    return mountFound, needSerenity

def loopEndurance(isDefault):
##    mountFound = False
    sleep(0.2,0.3)
    r,g,b = pyautogui.pixel(1030, 650)
    r2,g2,b2 = pyautogui.pixel(1095, 468)
    r3,g3,b3 = pyautogui.pixel(1030, 600)
    if (r != 204 and g != 246 and b != 0) and (r != 54 and g != 46 and b != 39) and (r3 == 204 and g3 == 246 and b3 == 0) and (r2 != 252 and g2 != 200 and b2 != 0):
        r,g,b = pyautogui.pixel(964,725)
        if (r not in range(22, 27) and g not in range(22, 27) and b not in range(18, 23)):
            if isDefault:
                return True, True
            else:
                keyboard.press_and_release("down")
                return False, False
        else:
            if not isDefault:
                transferToPen()
                waitForMount()
                return False, True
            keyboard.press_and_release("down")
            return False, True
    else:
        keyboard.press_and_release("down")
    return False, False

def loopMaturity(isDefault):
##    mountFound = False
    sleep(0.2,0.3)
    r4,g4,b4 = pyautogui.pixel(1030, 600)
    r2,g2,b2 = pyautogui.pixel(1030, 650)
    r,g,b = pyautogui.pixel(1030, 625)
    r3,g3,b3 = pyautogui.pixel(1095, 468)
    if (r != 204 and g != 246 and b != 0) and (r4 == 204 and g4 == 246 and b4 == 0) and (r2 == 204 and g2 == 246 and b2 == 0) and (r3 != 252 and g3 != 200 and b3 != 0):
        r,g,b = pyautogui.pixel(900,725)
        if (r != 204 and g != 246 and b != 0):
            if isDefault:
                return True, True
            else:
                keyboard.press_and_release("down")
                return False, False
        else:
            if not isDefault:
                transferToPen()
                waitForMount()
                return False, True
            keyboard.press_and_release("down")
            return False, True
    else:
        keyboard.press_and_release("down")
    return False, False

def loopLove(isDefault):
##    mountFound = False
    sleep(0.2,0.3)
    r2,g2,b2 = pyautogui.pixel(1030, 650)
    r,g,b = pyautogui.pixel(1030, 600)
    r3,g3,b3 = pyautogui.pixel(1095, 468)
    if (r != 204 and g != 246 and b != 0) and (r2 != 54 and g2 != 46 and b2 != 39) and (r3 != 252 and g3 != 200 and b3 != 0):
        r,g,b = pyautogui.pixel(967,725)
        if ((r != 204 and g != 246 and b != 0) and (r != 255 and g != 106 and b != 61)):
            if isDefault:
                return True, True
            else:
                keyboard.press_and_release("down")
                return False, False
        else:
            if not isDefault:
                transferToPen()
                waitForMount()
                return False, True
            keyboard.press_and_release("down")
            return False, True
    else:
        keyboard.press_and_release("down")
    return False, False

def transferToPen():
    sleep(0.2,0.3)
    keyboard.press_and_release("é")
    
def changeItems(item, isForced=False):
    sleep(0.4,0.5)
    pressEsc()
    goToThirdTab()
    if not isForced:
        r,g,b = pyautogui.pixel(1024,590)
        if item == "baffeur":
            if (r == 141 and g == 99 and b == 34):
                pyautogui.moveTo(500,500)
                clickOnPen()
                return
        elif item == "caresseur":
            if (r == 66 and g == 44 and b == 10):
                pyautogui.moveTo(500,500)
                clickOnPen()
                return
        elif item == "foudroyeur":
            if (r == 133 and g == 97 and b == 23) or (r == 151 and g == 141 and b == 68):
                pyautogui.moveTo(500,500)
                clickOnPen()
                return
        elif item == "mangeoire":
            if (r == 172 and g == 171 and b == 15):
                pyautogui.moveTo(500,500)
                clickOnPen()
                return
        elif item == "dragofesse":
            if (r == 93 and g == 69 and b == 14):
                pyautogui.moveTo(500,500)
                clickOnPen()
                return
        elif item == "abreuvoir":
            if (r == 127 and g == 110 and b == 49):
                pyautogui.moveTo(500,500)
                clickOnPen()
                return
    sleep(0.2,0.3)
    clickOnPen()
    emptyPen()
    pressEsc()
    clearPen()
##    clearBar()
    selectBreedingObj(item)
    pressEsc()
    fillPen()
    pyautogui.moveTo(500,500)
    clickOnPen()

def checkSerenityUp():
    sleep(0.2,0.3)
    click(765,667)
    sleep(0.4,0.5)
    click(605,675)
    waitForMount()
    for i in range(11):
        sleep(0.2,0.3)
        r,g,b = pyautogui.pixel(967,725)
        r2,g2,b2 = pyautogui.pixel(1111, 468)
        ##print("({},{},{}) ({},{},{}) on index {}".format(r,g,b,r2,g2,b2,i))
        if ((r != 204 and g != 246 and b != 0) and (r != 255 and g != 106 and b != 61)) and (r2 != 252 and g2 != 226 and b2 != 124):
            return True
        else:
            keyboard.press_and_release("down")
    return False

def checkSerenity(isDefault=True):
    pos, neg = False, False
    sleep(0.2,0.3)
    click(765,667)
    sleep(0.4,0.5)
    click(605,675)
    waitForMount()
    for i in range(11):
        sleep(0.2,0.3)
        r,g,b = pyautogui.pixel(900,725)
        r2,g2,b2 = pyautogui.pixel(1111, 468)
        if (r != 204 and g != 246 and b != 0) and (r2 != 252 and g2 != 226 and b2 != 124):
            if isDefault:
                return True
            else:
                r,g,b = pyautogui.pixel(965,725)
                if (r == 255 and g == 106 and b == 61):
                    pos = True
                else:
                    neg = True                
        keyboard.press_and_release("down")         
    if isDefault:
        return False
    else:
        return pos, neg

def checkSerenityDown():
    sleep(0.2,0.3)
    click(765,667)
    sleep(0.4,0.5)
    click(605,675)
    waitForMount()
    for i in range(11):
        sleep(0.2,0.3)
        r,g,b = pyautogui.pixel(964,725)
        r2,g2,b2 = pyautogui.pixel(1111, 468)
        if (r not in range(22, 27) and g not in range(22, 27) and b not in range(18, 23)) and (r2 != 252 and g2 != 226 and b2 != 124):
            return True
        else:
            keyboard.press_and_release("down")
    return False

def checkSerenityHigh(isDefault=False):
    sleep(0.2,0.3)
    click(765,667)
    sleep(0.4,0.5)
    click(605,675)
    waitForMount()
    for i in range(11):
        sleep(0.2,0.3)
        r,g,b = pyautogui.pixel(967,725)
        r2,g2,b2 = pyautogui.pixel(1111, 468)
        if not isDefault:
            r,g,b = pyautogui.pixel(900,725)
        if (r == 204 and g == 246 and b == 0) or (r2 == 252 and g2 == 226 and b2 == 124):
            keyboard.press_and_release("&")
            waitForMount()
        else:
            keyboard.press_and_release("down")

def checkEnergyInPen():
    sleep(0.2,0.3)
    click(765,667)
    sleep(0.4,0.5)
    click(605,675)
    waitForMount()
    for i in range(11):
        sleep(0.2,0.3)
        r,g,b = pyautogui.pixel(1111, 420)
        r2,g2,b2 = pyautogui.pixel(1111, 468)
        if (r == 224 and g == 249 and b == 104) or (r2 == 252 and g2 == 226 and b2 == 124):
            keyboard.press_and_release("&")
            waitForMount()
        else:
            keyboard.press_and_release("down")

def waitForMount(score=0):
    score += 1
    sleep(0.3,0.4)
    if score < 10 and pyautogui.locateOnScreen("smiley.PNG", region=(1055,675,110,110), confidence=0.8) == None:
        waitForMount(score)
        
def checkSerenityLow(isDefault=False):
    sleep(0.2,0.3)
    click(765,667)
    sleep(0.4,0.5)
    click(605,675)
    waitForMount()
    for i in range(11):
        sleep(0.2,0.3)
        r,g,b = pyautogui.pixel(964,725)
        r2,g2,b2 = pyautogui.pixel(1111, 468)
        if isDefault:
            condition = (r in range(22, 27) and g in range(22, 27) and b in range(18, 23)) or (r2 == 252 and g2 == 226 and b2 == 124)
        else:
            condition = (r != 255 and g != 106 and b != 61) or (r2 == 252 and g2 == 226 and b2 == 124)
        if condition:
            keyboard.press_and_release("&")
            waitForMount()
        else:
            keyboard.press_and_release("down")

def checkLME(LME):
    sleep(0.2,0.3)
    click(765,667)
    sleep(0.4,0.5)
    click(605,675)
    waitForMount()
    for i in range(11):
        sleep(0.2,0.3)
        if LME == "L":
            r,g,b = pyautogui.pixel(1020,600)
        elif LME == "M":
            r,g,b = pyautogui.pixel(1020,625)
        elif LME == "E":
            r,g,b = pyautogui.pixel(1020,650)
        else:
            print("error with LME ",LME)
        r2,g2,b2 = pyautogui.pixel(1111, 468)
        if (r == 204 and g == 246 and b == 0) or (r2 == 252 and g2 == 226 and b2 == 124):
            keyboard.press_and_release("&")
            waitForMount()
        else:
            keyboard.press_and_release("down")

def train(func, obj, flag=False, j=0):
    sleep(0.2,0.3)
    j+=1
    print("starting taining n°{}".format(j))
    if j >= 35:
        changeItems(obj, True)
        return
    for i in range(5):        
        keyboard.press_and_release("!")
        sleep(3,4)
        keyboard.press_and_release("ç")
        sleep(3,4)        
    sleep(2,3)
    func(flag) if flag else func()
    if pyautogui.locateOnScreen("empty2.0.PNG", region=(500,800,115,75), confidence=0.95) == None:
        train(func,obj,flag,j)
    else:
        print("all done with this training")
    
def checkForSterils():
    sleep(0.2,0.3)
    isEnd = False
    while not isEnd:
        loopSteril()
        r,g,b = pyautogui.pixel(764,478)
        if (r != 63 and g != 64 and b != 56):        
            isEnd = True
    for i in range(15):
        loopSteril()

def loopSerenityUp(default, moreInfo=False):
    i = 0
    isEnd = False
    mounts = 0
    goToThirdMount()
    waitForMount()
    while not isEnd and i < 300 and mounts < 10:
        i+=1
        res = loopSU(default)
        if res:
            mounts+=1
        r,g,b = pyautogui.pixel(764,478)
        if (r != 63 and g != 64 and b != 56):
            check = checkEnclos()
            if check:
                loopSerenityUp(default,moreInfo)
            isEnd = True
    if i >= 300:
        checkEnclos()
        loopSerenityUp(default,moreInfo)
    for i in range(15):
        if mounts >= 10:
            break
        res = loopSU(default)
        if res:
            mounts+=1
    if moreInfo:
        return True if mounts >= 10 else False

def loopEnergy(isMale):
    i = 0
    isEnd = False
    mounts = 0
    goToThirdMount()
    while not isEnd and i < 300 and mounts < 10:
        i+=1
        res = loopE(isMale)
        if res:
            mounts+=1
        r,g,b = pyautogui.pixel(764,478)
        if (r != 63 and g != 64 and b != 56):
            check = checkEnclos()
            if check:
                loopEnergy(isMale)
            isEnd = True
    if i >= 300:
        checkEnclos()
        loopEnergy(isMale)
    for i in range(15):
        if mounts >= 10:
            break
        res = loopE(isMale)
        if res:
            mounts+=1
    return True if mounts >= 10 else False
    

def loopSerenityDown(default, moreInfo=False):
    i = 0
    isEnd = False
    mounts = 0
    goToThirdMount()
    waitForMount()
    while not isEnd and i < 300 and mounts < 10:
        i+=1
        res = loopSD(default)
        if res:
            mounts+=1
        r,g,b = pyautogui.pixel(764,478)
        if (r != 63 and g != 64 and b != 56):
            check = checkEnclos()
            if check:
                loopSerenityDown(default,moreInfo)
            isEnd = True
    if i >= 300:
        checkEnclos()
        loopSerenityDown(default,moreInfo)
    for i in range(15):
        if mounts >= 10:
            break
        res = loopSD(default)
        if res:
            mounts+=1
    if moreInfo:
        return True if mounts >= 10 else False
    
def loopSU(isDefault):
    sleep(0.2,0.3)
    r2,g2,b2 = pyautogui.pixel(1095, 468)
    if isDefault:
        r3,g3,b3 = pyautogui.pixel(1030, 600)
        r,g,b = pyautogui.pixel(967,725)
        if (r3 != 204 and g3 != 246 and b3 != 0) and ((r != 204 and g != 246 and b != 0) and (r != 255 and g != 106 and b != 61)) and (r2 != 252 and g2 != 200 and b2 != 0):
            transferToPen()
            waitForMount()
            return True
        else:
            keyboard.press_and_release("down")
    else:
        r3,g3,b3 = pyautogui.pixel(1030, 625)
        r,g,b = pyautogui.pixel(900,725)
        r4,g4,b4 = pyautogui.pixel(964,725)
        if (r4 != 255 and g4 != 106 and b4 != 61) and (r3 != 204 and g3 != 246 and b3 != 0) and (r == 255 and g == 106 and b == 61) and (r2 != 252 and g2 != 200 and b2 != 0):
            transferToPen()
            waitForMount()
            return True
        else:
            keyboard.press_and_release("down")
    return False

def loopE(isMale):
    ##fixed the conditions in this one for future reference    
    sleep(0.2,0.3)
    isDefault = True
    r4,g4,b4 = pyautogui.pixel(1030, 600)
    r5,g5,b5 = pyautogui.pixel(1030, 650)
    r,g,b = pyautogui.pixel(1111, 420)
    r2,g2,b2 = pyautogui.pixel(1095, 468)
    r3,g3,b3 = pyautogui.pixel(1030, 625)
    if isMale and type(isMale) == bool:
        condition = pyautogui.locateOnScreen("male.png", region=(890,170,125,125), confidence=0.8) != None
    elif not isMale and type(isMale) == bool:
        condition = pyautogui.locateOnScreen("female.png", region=(890,170,125,125), confidence=0.8) != None
    else:
        isDefault = False
        condition = True
    if condition and (r4 == 204 and g4 == 246 and b4 == 0) and (r5 == 204 and g5 == 246 and b5 == 0) and (r != 224 or g != 249 or b != 104) and (r2 != 252 and g2 != 200 and b2 != 0) and (r3 == 204 and g3 == 246 and b3 == 0):
        if isDefault:
            transferToPen()
            waitForMount()
            return True
        else:
            male = pyautogui.locateOnScreen("male.png", region=(890,170,125,125), confidence=0.8) != None
            if male:
                keyboard.press_and_release("down")
                return True, False
            else:
                keyboard.press_and_release("down")
                return False, True
    else:
        keyboard.press_and_release("down")
    if isDefault:
        return False
    else:
        return False, False

def loopSD(isDefault): #might need to add endurance check for maturity
    sleep(0.2,0.3)
    r,g,b = pyautogui.pixel(964,725)
    r2,g2,b2 = pyautogui.pixel(1095, 468)
    r4,g4,b4 = pyautogui.pixel(1030, 600)
    if isDefault:
        r3,g3,b3 = pyautogui.pixel(1030, 650)
        if (r3 != 204 and g3 != 246 and b3 != 0) and (r4 == 204 and g4 == 246 and b4 == 0) and (r not in range(22, 27) and g not in range(22, 27) and b not in range(18, 23)) and (r2 != 252 and g2 != 200 and b2 != 0):
            transferToPen()
            waitForMount()
            return True
        else:
            keyboard.press_and_release("down")
    else:
        r3,g3,b3 = pyautogui.pixel(1030, 625)
        if (r3 != 204 and g3 != 246 and b3 != 0) and (r == 255 and g == 106 and b == 61)  and (r2 != 252 and g2 != 200 and b2 != 0):
            transferToPen()
            waitForMount()
            return True
        else:
            keyboard.press_and_release("down")
    return False

def upSerenity(default=True):
    ##trying out without sleep    
    changeItems("caresseur")
    goAgain = loopSerenityUp(default, True)
    train(checkSerenityHigh, "caresseur", default)
    return "Y" if goAgain else False

def downSerenity(default=True):
    changeItems("baffeur")
    goAgain = loopSerenityDown(default, True)
    train(checkSerenityLow, "baffeur", default)
    return "Y" if goAgain else False

def upMalesEnergy():
    changeItems("mangeoire")
    goAgain = loopEnergy(True)
    train(checkEnergyInPen, "mangeoire")
    return "Y" if goAgain else True

def transferLove():
    changeItems("dragofesse")
    goAgain = checkLove(False, True)
    train(checkLME,"dragofesse","L")
    return False if goAgain else "N"

def transferEndurance():
    changeItems("foudroyeur")
    goAgain = checkEndurance(False, True)
    train(checkLME,"foudroyeur","E")
    return False if goAgain else "N"

def transferMaturity():
    changeItems("abreuvoir")
    goAgain = checkMaturity(False, True)
    train(checkLME,"abreuvoir","M")
    return False if goAgain else "N"

def upFemalesEnergy():
    changeItems("mangeoire")
    goAgain = loopEnergy(False)
    train(checkEnergyInPen,"mangeoire")
    return False if goAgain else True

def upLove(isDefault=True):
    sleep(0.4,0.5)
    emptyPen()
    if isDefault:
        if isDefault == "Y":
            needLove, needSerenity = True, True
        elif isDefault == "N":
            needLove, needSerenity = False, False
        else:
            needLove, needSerenity = checkLove()
    else:
        needLove, needSerenity = True, False
    if needSerenity:
        repeatS = upSerenity()
        upLove(repeatS)
    elif needLove:
        skipS = transferLove()
        upLove(skipS)
    else:
        print("no need love")

def upEndurance(isDefault=True):
    sleep(0.4,0.5)
    emptyPen()
    if isDefault:
        if isDefault == "Y":
            needEndurance, needSerenity = True, True
        elif isDefault == "N":
            needEndurance, needSerenity = False, False
        else:
            needEndurance, needSerenity = checkEndurance()
    else:
        needEndurance, needSerenity = True, False
    if needSerenity:
        repeatS = downSerenity()
        upEndurance(repeatS)
    elif needEndurance:
        skipS = transferEndurance()
        upEndurance(skipS)
    else:
        print("no need endurance")

def upMaturity(isDefault=True, needPos=False, needNeg=False): #probably should have made a copy of before
    sleep(0.4,0.5)
    emptyPen()
    if isDefault:
        if isDefault == "Y":
            needMaturity, needSerenity = True, True
        elif isDefault == "N":
            needMaturity, needSerenity = False, False
        else:
            needMaturity, needSerenity = checkMaturity()
    else:
        needMaturity, needSerenity = True, False    
    if needSerenity:
        if isDefault == 'Y':
            pos, neg = needPos, needNeg
        else:
            pos, neg = checkSerenity(False)

        if pos:
            repeatS = downSerenity(False)#sort pos
            needPos = True if repeatS else False
        else:
            repeatS = False
            needPos = False
            
        if neg and not repeatS:
            repeatS = upSerenity(False)#sort neg
            needNeg = True if repeatS else False
        else:
            needNeg = False
        upMaturity(repeatS, needPos, needNeg)
    elif needMaturity:
        skipS = transferMaturity()
        upMaturity(skipS)
    else:
        print("no need maturity")

def upEnergy(isDefault=True):
    sleep(0.4,0.5)
    emptyPen()
    if isDefault == True:
        males, females = checkEnergy() #returns false??
    else:
        if isDefault == "Y":
            males, females = True, False
        else:
            males, females = False, True
    if males:
        repeatEM = upMalesEnergy()
        upEnergy(repeatEM)
    elif females:
        repeatEF = upFemalesEnergy()
        upEnergy(repeatEF)
    else:
        print("no need energy")

##def upEndurance(isDefault=True):
##    sleep(0.4,0.5)
##    emptyPen()
##    if isDefault:
##        if isDefault == "Y":
##            needEndurance, needSerenity = True, True
##        else:
##            needEndurance, needSerenity = checkEndurance()
##    else:
##        needEndurance, needSerenity = True, False
##    if needSerenity:
##        repeatS = downSerenity()
##        upEndurance(repeatS)
##    elif needEndurance:
##        skipS = transferEndurance()
##        upEndurance(skipS)
##    else:
##        print("no need endurance")

def mainTrainer():
    upLove()
    upEndurance()
    upMaturity()
    upEnergy()
    
def r():
    upMaturity()
    upEnergy()
##checkLME(LME)//checkSerenityLow()//checkSerenityHigh()
#red is (255,106,61)
##OBJ = ["baffeur","caresseur","foudroyeur","mangeoire","dragofesse"]
##(204, 246, 0) at pixel (962,725)//(22/26, 22/26, 18/22) at pixel (969,725) around 0
##changeItems(OBJ[4])
##upLove() #this works
##upEndurance() # this works
##upMaturity() #this works
##upEnergy() #this works
print("app Launched call mainTrainer() to start")