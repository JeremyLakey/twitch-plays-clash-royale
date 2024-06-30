import pyautogui
import time
from calibrate.util.beep import beep


def calibrate_open_command():
    time.sleep(5)
    pos1 = pyautogui.position()
    beep()

    time.sleep(4)
    pos2 = pyautogui.position()
    beep()

    time.sleep(4)
    pos3 = pyautogui.position()
    beep()

    time.sleep(4)
    pos4 = pyautogui.position()
    beep()

    time.sleep(4)
    pos5 = pyautogui.position()
    beep()

    f = open("../values/chests.txt", "w")
    f.write(str(pos1.x) + " " + str(pos1.y) + "\n" + str(pos2.x) + " " + str(pos2.y) + "\n" + str(pos3.x) + " " + str(
        pos3.y) + "\n" + str(pos4.x) + " " + str(pos4.y) + "\n" + str(pos5.x) + " " + str(pos5.y))
    f.close()


if __name__ == "__main__":
    calibrate_open_command()
