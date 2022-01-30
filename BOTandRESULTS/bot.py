import pyautogui
import time

time.sleep(10)
count=0

for i in range (15):
    count = count+1
    time.sleep(0.2)
    pyautogui.keyDown('alt')
    time.sleep(0.2)
    pyautogui.keyDown('tab')
    time.sleep(0.2)
    pyautogui.keyUp('tab')
    time.sleep(0.2)
    pyautogui.keyUp('alt')#go to the terminal
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
    #baixo(x=76, y=224)
    #cima(x=86, y=133)
    pyautogui.moveTo(x=76,y=224)
    pyautogui.mouseDown(button='left')
    pyautogui.dragTo(x=86,y=133,duration=2)
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

print('Done!')
