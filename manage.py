from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con
from gotobrak import goToBrakPen, clickOnPen, sleep, click
from mountTrainer import mainTrainer, goToThirdMount, waitForMount, emptyPen
from mountLeveLUp import mainLvlUp, train
import os
import traceback

def loopBreed():
    waitForMount()
    sleep(0.4,0.5)
    for i in range(5):
        keyboard.press_and_release("é")
        waitForMount()
    click(486,176)
    goToThirdMount()
    waitForMount()
    for i in range(5):
        keyboard.press_and_release("é")
        waitForMount()
    sleep(0.5,0.8)
    keyboard.press_and_release("!")
    sleep(3,4)
    keyboard.press_and_release("ç")
    sleep(3,4)
    keyboard.press_and_release("!")
    sleep(2,2.5)
    emptyPen()
    
def breed():
    sleep(0.2,0.3)
    empty = False
    i = 0
    click(551,137)
    while i < 10:
        i+=1
        sleep(0.2,0.3)
        pos = pyautogui.locateCenterOnScreen("feconde.PNG", confidence=0.8)
        if pos != None:
##            click(535,337)
            click(pos[0],pos[1])
            break
    if i == 10:
        return
    sleep(0.2,0.3)
    click(486,176)
    sleep(0.2,0.3)
    goToThirdMount()
    waitForMount()
    j = 0
    while j < 25:
        j+=1
        loopBreed()

def solo():
    sleep(0.2,0.3)
    click(696,1016)
    sleep(0.5,0.6)
    click(757,965)
    sleep(0.5,0.6)
    click(971,568)
    sleep(0.5,0.6)
    click(960,589)
    sleep(0.5,0.6)
    click(1167,565)
    
def dispo():
    sleep(0.2,0.3)
    click(696,1016)
    sleep(0.2,0.3)
    click(764,921)
    
def go():
    pyautogui.displayMousePosition()
            
##1198 241/ 59px
##pyautogui.moveTo(1198,241)
##time.sleep(2.5)
# img = pyautogui.screenshot()
# img.save(r"C:\Users\dylan\OneDrive\\Bureau\bots\errorScreenshot.png")
##
def test():
    if pyautogui.locateOnScreen("empty3.0.png", region=(1280,800,80,80), confidence=0.9) != None:
        print("gud")
    else:
        print("not gud")
        


def run():
    while True:
        shutdown = str(input("Do you want to shutdown? (y/n) "))
        if shutdown.lower() == "y" or shutdown.lower() == "n":
            break
        else:
            print("\nInvalid input try again \n")
    try:
        solo()
        mainTrainer()
        dispo()
        with open("Errors log.txt", "w") as file:
            file.write("All good")
        if shutdown.lower() == "y":
            os.system('shutdown -s')
    except Exception:
        with open("Errors log.txt", "w") as file:
            file.write(str(traceback.format_exc()))
        img = pyautogui.screenshot()
        img.save(r"C:\Users\dylan\OneDrive\\Bureau\bots\errorScreenshot.png")
        print(traceback.print_exc())
        if shutdown.lower() == "y":
            os.system('shutdown -s')
##run()