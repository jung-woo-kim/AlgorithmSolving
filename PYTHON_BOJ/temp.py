import datetime 
import time
import pyautogui
import urllib.request

month = {'Jan':'01', 'Feb':'02', 'Mar':'03', 'Apr':'04', 'May':'05', 'Jun':'06', \
    'Jul':'07', 'Aug':'08', 'Sep':'09', 'Oct':'10', 'Nov':'11', 'Dec':'12'}

url = 'http://www.google.com'
date = urllib.request.urlopen(url).headers['Date']
#d, m, y, hour, min, sec = date[:2], month[date[3:6]], date[7:11], date[12:14], date[15:17], date[18:]
print(date)

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