import pyautogui
from time import sleep
import keyboard

#grag mouse to upper-left corner to sop execution
pyautogui.FAILSAFE=True
#pause after every task
pyautogui.PAUSE = 0.1

class coords():
    braceletX = 296
    braceletY = 118

    takebraceletX = 296
    takebraceletY = 205

    etherX = 344
    etherY = 118

    takeetherX = 344
    takeetherY = 155

    invetherX = 904
    invetherY = 683

#take 24 bracelets
def takebracelets():
    pyautogui.moveTo(coords.braceletX, coords.braceletY, .4, pyautogui.easeInOutQuad)
    pyautogui.click(button='right')
    pyautogui.moveTo(coords.takebraceletX, coords.takebraceletY, .4, pyautogui.easeInOutQuad)
    pyautogui.click()

#take one ether
def takeether():
    pyautogui.moveTo(coords.etherX, coords.etherY, .4, pyautogui.easeInOutQuad)
    pyautogui.click(button='right')
    pyautogui.moveTo(coords.takeetherX, coords.takeetherY, .4, pyautogui.easeInOutQuad)
    pyautogui.click()

#click ether in inventory
def clickether():
    pyautogui.moveTo(coords.invetherX, coords.invetherY, .4, pyautogui.easeInOutQuad)
    pyautogui.click()

def ench():
    
    takebracelets()
    takeether()
    
    for i in range(0, 24):
        #close bank
        pyautogui.moveTo(645, 42, .2, pyautogui.easeInOutQuad)
        pyautogui.click()
        clickether()
        #move to top of inventory
        pyautogui.moveTo(904, 463, .1, pyautogui.easeInOutQuad)
        
        j=(i-i%4)/4
        
        if j == 0:
            if i-(i//4*4)== 0:
                
                pyautogui.click()
            
            elif i-(i//4*4)==1:
                
                pyautogui.move(42, 0)
                pyautogui.click()
            
            elif i-(i//4*4)==2:
                
                pyautogui.move(42, 0)
                pyautogui.move(42, 0)
                pyautogui.click()
            
            elif i-(i//4*4)==3:
                
                pyautogui.move(42, 0)
                pyautogui.move(42, 0)
                pyautogui.move(42, 0)
                
                pyautogui.click()
        elif j == 1:
            pyautogui.move(0, 37)
            if i-(i//4*4)== 0:
                
                pyautogui.click()
            
            elif i-(i//4*4)==1:
                
                pyautogui.move(42, 0)
                pyautogui.click()
            
            elif i-(i//4*4)==2:
                
                pyautogui.move(42, 0)
                pyautogui.move(42, 0)
                pyautogui.click()
            
            elif i-(i//4*4)==3:
                
                pyautogui.move(42, 0)
                pyautogui.move(42, 0)
                pyautogui.move(42, 0)
                pyautogui.click()
        
        elif j == 2:
            pyautogui.move(0, 37)
            pyautogui.move(0, 37)
            if i-(i//4*4)== 0:
                
                pyautogui.click()
            
            elif i-(i//4*4)==1:
                
                pyautogui.move(42, 0)
                pyautogui.click()
            
            elif i-(i//4*4)==2:
                
                pyautogui.move(42, 0)
                pyautogui.move(42, 0)
                pyautogui.click()
            
            elif i-(i//4*4)==3:
                
                pyautogui.move(42, 0)
                pyautogui.move(42, 0)
                pyautogui.move(42, 0)
                pyautogui.click()
        
        elif j == 3:     
            pyautogui.move(0, 37)
            pyautogui.move(0, 37)
            pyautogui.move(0, 37)
            if i-(i//4*4)== 0:
                
                pyautogui.click()
            
            elif i-(i//4*4)==1:
                
                pyautogui.move(42, 0)
                pyautogui.click()
            
            elif i-(i//4*4)==2:
                
                pyautogui.move(42, 0)
                pyautogui.move(42, 0)
                pyautogui.click()
            
            elif i-(i//4*4)==3:
                
                pyautogui.move(42, 0)
                pyautogui.move(42, 0)
                pyautogui.move(42, 0)
                pyautogui.click()
        
        elif j == 4:
            pyautogui.move(0, 37)
            pyautogui.move(0, 37)
            pyautogui.move(0, 37)
            pyautogui.move(0, 37)
            if i-(i//4*4)== 0:
                
                pyautogui.click()
            
            elif i-(i//4*4)==1:
                
                pyautogui.move(42, 0)
                pyautogui.click()
            
            elif i-(i//4*4)==2:
                
                pyautogui.move(42, 0)
                pyautogui.move(42, 0)
                pyautogui.click()
            
            elif i-(i//4*4)==3:
                
                pyautogui.move(42, 0)
                pyautogui.move(42, 0)
                pyautogui.move(42, 0)
                pyautogui.click()
        
        elif j == 5:
            pyautogui.move(0, 37)
            pyautogui.move(0, 37)
            pyautogui.move(0, 37)
            pyautogui.move(0, 37)
            pyautogui.move(0, 37)
            if i-(i//4*4)== 0:
                
                pyautogui.click()
            
            elif i-(i//4*4)==1:
                
                pyautogui.move(42, 0)
                pyautogui.click()
            
            elif i-(i//4*4)==2:
                
                pyautogui.move(42, 0)
                pyautogui.move(42, 0)
                pyautogui.click()
            
            elif i-(i//4*4)==3:
                
                pyautogui.move(42, 0)
                pyautogui.move(42, 0)
                pyautogui.move(42, 0)
                pyautogui.click()
        
        #change to stop    
        if i == 100:
            exit()

        #opening bank
        pyautogui.moveTo(494, 370, .4, pyautogui.easeInOutQuad)
        pyautogui.click()
        sleep(1)
        
        if i != 23:
            takeether()

def alch():
    for i in range(0,24):
        #clicking alch spell
        pyautogui.moveTo(1046, 549, .5, pyautogui.easeInOutQuad)
        pyautogui.click()
        sleep(.5)
        #clicking bracelet
        pyautogui.moveTo(1030, 644, .5, pyautogui.easeInOutQuad)
        pyautogui.click()
        sleep(1)


running = False

while True:
    
    if keyboard.is_pressed('n'):
        print('Running.')
        running = True
    
    if running == True:
        
        for i in range(0,3):
            ench()
            #take nature runes
            pyautogui.moveTo(247, 176, .5, pyautogui.easeInOutQuad)
            pyautogui.click()
            #close bank
            pyautogui.moveTo(645, 42, .4, pyautogui.easeInOutQuad)
            pyautogui.click()
            #open spell book
            pyautogui.moveTo(1065, 420, .4, pyautogui.easeInOutQuad)
            pyautogui.click()
            
            alch()

            #open inventory
            pyautogui.moveTo(970, 420, .3, pyautogui.easeInOutQuad)
            pyautogui.click()

            #open bank
            pyautogui.moveTo(494, 370, .4, pyautogui.easeInOutQuad)
            pyautogui.click()

            #deposit nature runes and money
            pyautogui.moveTo(coords.invetherX, coords.invetherY, .5, pyautogui.easeInOutQuad)
            pyautogui.click()
            pyautogui.moveTo(904, 463, .5, pyautogui.easeInOutQuad)
            pyautogui.click()

        running=False


