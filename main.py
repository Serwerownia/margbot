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
#check = pyautogui.locateOnScreen("targets/test.png")
screen = pyautogui.screenshot('zdj.png',region=(250,205,1420,760))
time.sleep(32)
screen1 = pyautogui.screenshot('zdj1.png',region=(250,205,1420,760))

img1 = cv2.imread('zdj.png')
img2 = cv2.imread('zdj1.png')
img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

def mse(img1, img2):
   h, w = img1.shape
   diff = cv2.subtract(img1, img2)
   err = np.sum(diff**2)
   mse = err/(float(h*w))
   return mse, diff

error, diff = mse(img1, img2)

diff = cv2.Canny(diff, 127, 127 * 2)

contours, _ = cv2.findContours(diff, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

contours_poly = [None]*len(contours)
boundRect = [None]*len(contours)
centers = [None]*len(contours)
radius = [None]*len(contours)
for i, c in enumerate(contours):
    contours_poly[i] = cv2.approxPolyDP(c, 3, True)
    boundRect[i] = cv2.boundingRect(contours_poly[i])
    centers[i], radius[i] = cv2.minEnclosingCircle(contours_poly[i])

print("Image matching Error between the two images:",error)

#cv2.circle(diff,(int(centers[0][0]), int(centers[0][1])), 10 , (255,0,0) ,-1)

pyautogui.moveTo(int(centers[0][0]+250), int(centers[0][1]+200))
time.sleep(1)
zuk = pyautogui.locateCenterOnScreen("zuk.png")
time.sleep(1)
if(zuk != None):
    pyautogui.click()
    time.sleep(1)
    pyautogui.hotkey("f")
    time.sleep(1)
    pyautogui.hotkey("z")


#cv2.imshow("difference", diff)
cv2.waitKey(0)
#cv2.destroyAllWindows()


