import pyautogui
import time


def calibrate_safespot():
    time.sleep(5)
    pos1 = pyautogui.position()
    pyautogui.click()

    f = open("../values/safespot.txt", "w")
    f.write(str(pos1.x) + " " + str(pos1.y))
    f.close()


if __name__ == "__main__":
    calibrate_safespot()
