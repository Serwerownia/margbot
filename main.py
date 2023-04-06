import datetime
import pyautogui
from threading import Thread
import customtkinter
import numpy as np
import cv2
import time

pyautogui.FAILSAFE = False

#screen = pyautogui.screenshot('zdj.png',region=(250,205,1420,760))
#screen1 = pyautogui.screenshot('zdj1.png',region=(250,205,1420,760))
#zdj = pyautogui.screenshot('zdj.png',region=(250,205,1420,760))


customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

#future_time = datetime.datetime.now() + datetime.timedelta(seconds=30)
bot_run = True

screen_X = 250
screen_Y = 205
screen_W = 1420
screen_H = 760


bot_run = True

def BotLoop():
    global future_time
    current_img = None
    priev_img = Screenshot(screen_X, screen_Y, screen_W, screen_H)
    priev_img = cv2.cvtColor(priev_img, cv2.COLOR_BGR2GRAY)
    while(bot_run == True):
        """
        while datetime.datetime.now() >= future_time:
            pyautogui.keyDown("a")
            time.sleep(0.5)
            pyautogui.keyUp("a")
            pyautogui.keyDown("d")
            time.sleep(0.5)
            pyautogui.keyUp("d")

            future_time = datetime.datetime.now() + datetime.timedelta(seconds=30)
        """

        current_img = Screenshot(screen_X, screen_Y, screen_W, screen_H)
        time.sleep(3)
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

        boss = pyautogui.locateCenterOnScreen("boss.png", confidence=0.8)
        if (boss != None):
            pyautogui.click()
            time.sleep(1)
            pyautogui.hotkey("f")
            time.sleep(1)
            pyautogui.hotkey("z")


        pot = pyautogui.locateCenterOnScreen("potwierdz.png")
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

new_thread = None
def Main():
    global bot_run
    global new_thread

    root = customtkinter.CTk()
    root.geometry("230x300")

    frame = customtkinter.CTkFrame(master=root)
    frame.pack(pady=20, padx=60, fill="both", expand=True)


    label = customtkinter.CTkLabel(master=frame, text="Bot")
    label.pack(pady=12, padx=10)

    global status
    status = customtkinter.CTkLabel(master=frame, text="Bot jest OFF")
    status.pack(pady=6, padx=5)

    """
    def Test():
        print("lol")

    button = customtkinter.CTkButton(master=frame, text="Test", command=Test)
    button.pack(pady=12, padx=10)
    """

    def Start():
        global new_thread
        new_thread = Thread(target=BotLoop)
        new_thread.start()

        status.configure(text="Bot jest ON")
        status.pack(pady=6, padx=5)

    button = customtkinter.CTkButton(master=frame, text="Start", command=Start)
    button.pack(pady=12, padx=10)

    def Exit():
        global bot_run
        bot_run = False

        status.configure(text="Bot jest OFF")
        status.pack(pady=6, padx=5)

    button = customtkinter.CTkButton(master=frame, text="Stop", command=Exit)
    button.pack(pady=12, padx=10)

    root.mainloop()
    if(new_thread!=None):
        new_thread.join()

if __name__ == "__main__":
    Main()

#cv2.imshow("difference", diff)
cv2.waitKey(0)
#cv2.destroyAllWindows()
