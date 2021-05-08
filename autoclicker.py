#! python3
import pyautogui, sys
import time
import keyboard

def autoclick():
    pyautogui.click(button='left')

print('Autoclicker')
print('-----------')
print('Press Ctrl-C to quit the program')
print('To toggle autoclick press q')

isRunning=False

while True:
    while True:
        try:
            if keyboard.is_pressed('q'):
                if isRunning:
                    isRunning = False
                    print('Autoclicker is off!')
                else:
                    isRunning = True
                    print('Autoclicker is on!')
                time.pause(1)
                
                break
            else:
                if isRunning:
                    autoclick()
        except:
            break


