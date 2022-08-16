import datetime 
import time
import pyautogui

endhope=False
while not endhope:
    tim=datetime.datetime.now()
    if tim.second>=59 and tim.microsecond>300000:
        pyautogui.click(pyautogui.position())
        endhope=True
        print(tim)
    else:
        time.sleep(0.1)
        print(pyautogui.position())
        print(tim)