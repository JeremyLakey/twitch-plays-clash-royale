import pyautogui
import time


def calibrate_edit_command():
    time.sleep(5)
    pos1 = pyautogui.position()
    pyautogui.click()

    time.sleep(4)
    pos2 = pyautogui.position()
    pyautogui.click()

    f = open("../values/editDeck.txt", "w")
    f.write(str(pos1.x) + " " + str(pos1.y) + "\n" + str(pos2.x) + " " + str(pos2.y))
    f.close()


if __name__ == "__main__":
    calibrate_edit_command()
