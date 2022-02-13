#BOT THAT TRANSFERS THE DATA TO EXCEL

import pyautogui
import time

time.sleep(10)
count=0

for i in range (15):
    count+=1
    print (count,' execução')
    time.sleep(0.2)
    pyautogui.keyDown('alt')
    time.sleep(0.2)
    pyautogui.keyDown('tab')
    time.sleep(0.2)
    pyautogui.keyUp('tab')
    time.sleep(0.2)
    pyautogui.keyUp('alt')
    time.sleep(1)
    for j in range(7):
        pyautogui.press('down')
    time.sleep(0.2)
    j=0
    for j in range(20):
        pyautogui.press('right')
    time.sleep(1)
    pyautogui.keyDown('shift')
    j=0
    for j in range(4):
        pyautogui.press('right')
    pyautogui.keyUp('shift')
    time.sleep(0.2)
    pyautogui.keyDown('ctrl')
    time.sleep(0.2)
    pyautogui.press('c')
    time.sleep(0.2)
    pyautogui.keyUp('ctrl')
    time.sleep(0.2)
    pyautogui.keyDown('alt')
    time.sleep(0.2)
    pyautogui.keyDown('tab')
    time.sleep(0.2)
    pyautogui.keyUp('tab')
    time.sleep(0.2)
    pyautogui.keyUp('alt')
    time.sleep(1)
    pyautogui.press('backspace')
    pyautogui.keyDown('ctrl')
    time.sleep(0.2)
    pyautogui.press('v')
    time.sleep(0.2)
    pyautogui.keyUp('ctrl')
    time.sleep(0.2)
    pyautogui.press('0')
    pyautogui.keyDown('alt')
    time.sleep(0.2)
    pyautogui.keyDown('tab')
    time.sleep(0.2)
    pyautogui.keyUp('tab')
    time.sleep(0.2)
    pyautogui.keyUp('alt')
    time.sleep(1)
    j=0
    for j in range(21):
        pyautogui.press('left')
    time.sleep(0.2)
    j=0
    for j in range(2):
        pyautogui.press('down')
    time.sleep(0.2)
    j=0
    for j in range(30):
        pyautogui.press('right')
    time.sleep(0.2)
    pyautogui.keyDown('shift')
    j=0
    for j in range(4):
        pyautogui.press('right')
    pyautogui.keyUp('shift')
    time.sleep(0.2)
    pyautogui.keyDown('ctrl')
    time.sleep(0.2)
    pyautogui.press('c')
    time.sleep(0.2)
    pyautogui.keyUp('ctrl')
    j=0
    for j in range(31):
        pyautogui.press('left')
    pyautogui.keyDown('alt')
    time.sleep(0.2)
    pyautogui.keyDown('tab')
    time.sleep(0.2)
    pyautogui.keyUp('tab')
    time.sleep(0.2)
    pyautogui.keyUp('alt')
    time.sleep(1)
    pyautogui.press('right')
    pyautogui.press('backspace')
    pyautogui.keyDown('ctrl')
    time.sleep(0.2)
    pyautogui.press('v')
    time.sleep(0.2)
    pyautogui.keyUp('ctrl')
    time.sleep(0.2)
    pyautogui.press('down')
    pyautogui.press('left')