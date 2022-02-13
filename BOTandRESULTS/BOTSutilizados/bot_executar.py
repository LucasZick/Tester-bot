#A bot that runs the run-contest file on sourdough/datagrump repo, it needs to be adapted to the size of the screen. Just used to test my skills and also help me in a class work that demands so much time manually.
#
#The .txt files are the results of the bot cicles, it runs run-contest 15 times wich each window size from 10 to 100, five by five, like 10,15,20,25...100.
#
#Run this code and open the .txt file that you want to save the code, your alt+tab sequence needs to be >.txt file >bash.

import pyautogui
import time

time.sleep(10)#wait to do the preparation after running the code(open the apps in the correct order)
count=0#number of rounds done

for i in range (15):
    count = count+1
    time.sleep(0.2)
    pyautogui.keyDown('alt')
    time.sleep(0.2)
    pyautogui.keyDown('tab')
    time.sleep(0.2)
    pyautogui.keyUp('tab')
    time.sleep(0.2)
    pyautogui.keyUp('alt')#go to the bash
    time.sleep(5)
    pyautogui.press('enter')
    time.sleep(0.5)
    pyautogui.write('clear')#clear to maintain the same pixels of click every try
    time.sleep(0.2)
    pyautogui.press('enter')
    time.sleep(1.5)
    pyautogui.write('./run-contest LucasZick')#run the archive
    time.sleep(0.2)
    pyautogui.press('enter')
    time.sleep(180)#wait the finishing of the process
    #bottom(x=76, y=224)
    #upper(x=86, y=133)
    pyautogui.moveTo(x=76,y=224)#use cursorposition.py on this repo to find exactly the values, thats probably not the same of my screen
    pyautogui.mouseDown(button='left')
    pyautogui.dragTo(x=86,y=133,duration=2)#use cursorposition.py on this repo to find exactly the values
    pyautogui.mouseUp(button='left')#select the results
    pyautogui.click(button='right')#open the menu of the selection
    time.sleep(0.2)
    pyautogui.press('down')
    time.sleep(0.2)
    pyautogui.press('enter')#select copy
    time.sleep(0.2)
    pyautogui.keyDown('alt')
    time.sleep(0.2)
    pyautogui.press('tab')
    time.sleep(0.2)
    pyautogui.keyUp('alt')#return to the txt file
    time.sleep(1.5)
    pyautogui.write('RESULTADO '+ str(count))#says whats the position of the result
    for k in range(2):
        time.sleep(0.2)
        pyautogui.press('enter')
        time.sleep(0.2)
    pyautogui.keyDown('ctrl')
    time.sleep(0.2)
    pyautogui.press('v')#paste the result
    time.sleep(0.2)
    pyautogui.keyUp('ctrl')
    for j in range(3):
        time.sleep(0.2)
        pyautogui.press('enter')
        time.sleep(0.2)
    time.sleep(1.5)
    pyautogui.keyDown('ctrl')
    time.sleep(0.2)
    pyautogui.press('s')
    time.sleep(0.2)
    pyautogui.keyUp('ctrl')#save the archive every round

print('Done!')#show that the process ended succesfully
