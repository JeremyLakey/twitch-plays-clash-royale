import pyautogui
import time
from calibrate.util.beep import beep


def calibrate_scroll():
    time.sleep(5)
    pos1 = pyautogui.position()
    beep()

    time.sleep(4)
    pos2 = pyautogui.position()
    beep()

    f = open("../values/scroll.txt", "w")
    f.write(str(pos1.x) + " " + str(pos1.y) + "\n" + str(pos2.x) + " " + str(pos2.y))
    f.close()


if __name__ == "__main__":
    calibrate_scroll()
