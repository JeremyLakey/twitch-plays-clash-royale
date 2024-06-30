import pyautogui
import time
from calibrate.util.beep import beep


def calibrate_emotes():
    time.sleep(5)
    pos1 = pyautogui.position()
    beep()

    time.sleep(3)
    pos2 = pyautogui.position()
    beep()

    time.sleep(5)
    pos3 = pyautogui.position()
    beep()

    f = open("../values/emote-cords.txt", "w")
    f.write(str(pos1.x) + " " + str(pos1.y) + "\n" + str(pos2.x) + " " + str(pos2.y) + "\n" + str(pos3.x) + " " + str(pos3.y))
    f.close()


if __name__ == "__main__":
    calibrate_emotes()
