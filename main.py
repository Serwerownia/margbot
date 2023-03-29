import pyautogui
from threading import Thread
import pyscreeze
import numpy as np
import cv2
import time

#screen = pyautogui.screenshot('zdj.png',region=(250,205,1420,760))
#screen1 = pyautogui.screenshot('zdj1.png',region=(250,205,1420,760))
zdj = pyautogui.screenshot('zdj.png',region=(250,205,1420,760))

screen_X = 250
screen_Y = 205
screen_W = 1420
screen_H = 760

bot_run = True

def BotLoop():
    current_img = None
    priev_img = Screenshot(screen_X, screen_Y, screen_W, screen_H)
    priev_img = cv2.cvtColor(priev_img, cv2.COLOR_BGR2GRAY)
    while(bot_run == True):
        current_img = Screenshot(screen_X, screen_Y, screen_W, screen_H)
        time.sleep(5)
        current_img = cv2.cvtColor(current_img, cv2.COLOR_BGR2GRAY)

        diff = Diff(current_img, priev_img)
        diff = cv2.Canny(diff, 127, 127 * 2)

        priev_img = current_img

        centers = LocateObj(diff)

        if(len(centers) == 0):
            print("nie ma roznic")
            continue

        middle = (screen_W / 2, screen_H / 2)
        def DisToMid(point):
            return ((middle[0] - point[0]) ** 2 + (middle[1] - point[1]) ** 2) ** 0.5
        centers = sorted(centers, key=DisToMid)

        pyautogui.moveTo(int(centers[0][0] + 250), int(centers[0][1] + 205))

        time.sleep(1)
        zuk = pyautogui.locateCenterOnScreen("zuk.png")
        time.sleep(1)
        if (zuk != None):
            pyautogui.click()
            time.sleep(1)
            pyautogui.hotkey("f")
            time.sleep(1)
            pyautogui.hotkey("z")

        time.sleep(1)
        pot = pyautogui.locateCenterOnScreen("potwierdz.png")
        time.sleep(1)
        if (pot != None):
            pyautogui.moveTo(int(pot[0]), int(pot[1]))
            pyautogui.click()

        pyautogui.moveTo(1,1)

def Screenshot(x,y,w,h):
    screenshot = pyautogui.screenshot(region=(x,y,w,h))
    image = np.array(screenshot)
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    return image

def Diff(img1 , img2):
    return cv2.subtract(img1 , img2)

def LocateObj(diff):
    contours, _ = cv2.findContours(diff, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours_poly = [None] * len(contours)
    boundRect = [None] * len(contours)
    centers = [None] * len(contours)
    radius = [None] * len(contours)

    for i, c in enumerate(contours):
        contours_poly[i] = cv2.approxPolyDP(c, 3, True)
        boundRect[i] = cv2.boundingRect(contours_poly[i])
        centers[i], radius[i] = cv2.minEnclosingCircle(contours_poly[i])

    return centers

def Main():
    global bot_run
    new_thread = Thread(target=BotLoop)
    new_thread.start()
    while(True):
        xD = input()
        if(xD == 'q'):
            bot_run = False
            break

    new_thread.join()

Main()
#cv2.imshow("difference", diff)
cv2.waitKey(0)
#cv2.destroyAllWindows()




