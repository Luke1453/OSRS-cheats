import pyautogui
from time import sleep
import keyboard
import os
import sys

#grag mouse to upper-left corner to stop execution
pyautogui.FAILSAFE=True
#pause after every task
pyautogui.PAUSE = 0.2

class coords():
    herbX = 400
    herbY = 118

#take 24 herbs
def takeherbs():
    pyautogui.moveTo(coords.herbX, coords.herbY, .1, pyautogui.easeInOutQuad)
    pyautogui.click()

def closebank():
    pyautogui.moveTo(645, 42, .1, pyautogui.easeInOutQuad)
    pyautogui.click()
    sleep(1)

def clean():
    #move to first item in inventory
    pyautogui.moveTo(906, 462, .1, pyautogui.easeInOutQuad)

    for i in range(0,7):
        pyautogui.click()
        pyautogui.move(0, 36)
    
    #move to 2nd item in inventory
    pyautogui.moveTo(906, 462, .1, pyautogui.easeInOutQuad)
    pyautogui.move(42, 0)

    for i in range(0,7):
        pyautogui.click()
        pyautogui.move(0, 36)
    
    #move to 3rd item in inventory
    pyautogui.moveTo(906, 462, .1, pyautogui.easeInOutQuad)
    pyautogui.move(42, 0)
    pyautogui.move(42, 0)

    for i in range(0,7):
        
        pyautogui.click()
        pyautogui.move(0, 36)
    
    #move to 4th item in inventory
    pyautogui.moveTo(906, 462, .1, pyautogui.easeInOutQuad)
    pyautogui.move(42, 0)
    pyautogui.move(42, 0)
    pyautogui.move(42, 0)

    for i in range(0,7):
        pyautogui.click()
        pyautogui.move(0, 36)

def deposit():
    #opening the bank
    pyautogui.moveTo(494, 370, .1, pyautogui.easeInOutQuad)
    pyautogui.click()
    sleep(1)
    #deposit
    pyautogui.moveTo(906, 462, .1, pyautogui.easeInOutQuad)
    pyautogui.click()

am=int(input("Enter amount of herbs: "))
inv=am//28

for i in range(0, inv):
    takeherbs()
    closebank()
    clean()
    deposit()

#python = sys.executable
#os.execl(python, python, * sys.argv)