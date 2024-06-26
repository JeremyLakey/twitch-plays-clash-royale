import pyautogui
import time
from calibrate.beep import beep


def calibrate_safespot():
    time.sleep(5)
    pos1 = pyautogui.position()
    beep()

    f = open("../values/safespot.txt", "w")
    f.write(str(pos1.x) + " " + str(pos1.y))
    f.close()


if __name__ == "__main__":
    calibrate_safespot()
