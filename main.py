import pyautogui
import pyscreeze
import numpy as np
import cv2
import time


#res = pyatogui.locateOnScreen("nazwa pliku png") wyszkuje danego obrazu z liku na ekranie
#print(pyautogui.center(res)) printuje koordy na ktorych znajduje sie dany obraz taki sam jak w pliku
#pyautogui.moveTo() przesowa kursor w dana lokacje na ekranie
#res = pyautoguiv.locateCensterOnScreen("nazwa pliku png") znajduje srodek zdjecia na ekranie

#res = pyautogui.locateCenterOnScreen("targets/mob.png")
#print(pyscreeze.locateCenterOnScreen("swierszcz.png"))
check = pyautogui.locateOnScreen("targets/test.png") 
screen = pyautogui.screenshot('zdj.png',region=(250,205,875,510))
time.sleep(10)
screen1 = pyautogui.screenshot('zdj1.png',region=(250,205,875,510))

img1 = cv2.imread('zdj.png')
img2 = cv2.imread('zdj1.png')
img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

def mse(img1, img2):
   h, w = img1.shape
   diff = cv2.subtract(img1, img2)
   err = np.sum(diff**2)
   mse = err/(float(h*w))
   return mse

 = mse(img1, img2)
#print("Image matching Error between the two images:",error)

cv2.imshow("difference", diff)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

"""
if(screen == screen1):
    print("takie same")
else:
    print("rozne")


if (res != None):
    pyautogui.moveTo(res)
    time.sleep(2)
    pyautogui.click()
    time.sleep(5)
    pyautogui.hotkey("f")
    time.sleep(5)
    pyautogui.hotkey("z")
elif (res1 != None):
    pyautogui.moveTo(res1)
    time.sleep(2)
    pyautogui.click()
    time.sleep(5)
    pyautogui.hotkey("f")
    time.sleep(5)
    pyautogui.hotkey("z")
else:
    print("gagri")
"""

#if(x == None & y == None):
#    exit("could not find mb")

#pyscreeze.click(x,y)
"""
time.sleep(2)
pyautogui.hotkey("f")
time.sleep(2)
pyautogui.hotkey("z")
"""


