import os
import mss
import mss.tools
from PIL import Image, ImageChops
import math, operator
from functools import reduce
from datetime import datetime
from time import sleep
import pyautogui
import keyboard
from random import randint, uniform, choice

#what to grab
monitor = {"top": 208, "left": 489, "width": 77, "height": 81}
winecount=0

class delays():
    beforeclickmin = .2 
    beforeclickmax = .8


class coords():
    wineYmin = 211
    wineYmax = 286
    wineXmax = 563
    wineXmin = 492

    grabYmin = 492
    grabYmax = 507
    grabXmin = 1010
    grabXmax = 1026

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

def equal(im1, im2):
    h1 = Image.open(im1).histogram()
    h2 = Image.open(im2).histogram()
     
    rms = math.sqrt(reduce(operator.add,
    	map(lambda a,b: (a-b)**2, h1, h2))/len(h1))

    return rms

def imagegrab():
    with mss.mss() as sct:
    
        time = datetime.now().strftime("%H~%M~%S~%f")
        new = "Wine-"+time+".png"

        #screenshot
        sct_img = sct.grab(monitor)
    
        # Save to the picture file
        mss.tools.to_png(sct_img.rgb, sct_img.size, output=new)

    return new

def detection(): 
    while True:
        #sleep(.1)
        prew = imagegrab()
        sleep(.2)
        new = imagegrab()

        if keyboard.is_pressed('alt+n'):
            exit()

        if equal(prew,new) != 0:
            print("grabbing")
            os.remove(prew)
            os.remove(new)
            return True

        os.remove(prew)
        os.remove(new)

running = False

while True:
    
    if keyboard.is_pressed('n'):
        print('Running.')
        running = True
    
    while running == True:
        
        if keyboard.is_pressed('alt+n'):
            exit()
        
        if detection() == True:
            clickTeleGrab()
            GrabWine()
            winecount +=1
            print('Wine count: %d' %winecount)
            sleep(4)