from random import randint, uniform, choice
from time import sleep
import pyautogui
import keyboard

class delays():
    beforeclickmin = .5 
    beforeclickmax = 1.0


class coords():
    wineYmin = 325
    wineYmax = 346
    wineXmax = 544
    wineXmin = 523

    grabYmin = 492
    grabYmax = 507
    grabXmin = 1010
    grabXmax = 1029

    wineX = list(range(wineXmin, wineXmax))
    wineY = list(range(wineYmin, wineYmax))

    grabX = list(range(grabXmin, grabXmax))
    grabY = list(range(grabYmin, grabYmax))

def GrabWine():
    pyautogui.moveTo(choice(coords.wineX), choice(coords.wineY), .2, pyautogui.easeInOutQuad)
    sleep(round(uniform(delays.beforeclickmin,delays.beforeclickmax), 3))
    pyautogui.click()

def clickTeleGrab():
    pyautogui.moveTo(choice(coords.grabX), choice(coords.grabY), .2, pyautogui.easeInOutQuad)
    sleep(round(uniform(delays.beforeclickmin,delays.beforeclickmax), 3))
    pyautogui.click()

def actions():
    clickTeleGrab()
    sleep(29.0 + round(uniform(delays.beforeclickmin,delays.beforeclickmax), 3)) #29.0 sec for spawn
    GrabWine()
    
running = False
winecount = 0

print('Press ctrl+F1 to start.')
print('Press ctrl+F2 to pause.')
print('Press ctrl+F3 to exit.')
print('----------------------------------------------') 

while True:
    
    if keyboard.is_pressed('ctrl+F1'):
        print('Running.')
        running = True
    
    while running == True:
        
        if keyboard.is_pressed('ctrl+F3'):
            exit()
        
        if keyboard.is_pressed('ctrl+F2'):
            print('Pause.')
            winecount = 0
            running = False
            break

        actions()
        winecount +=1
        print('Wine count: %d' %winecount)