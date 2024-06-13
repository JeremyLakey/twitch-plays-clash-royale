import pyautogui
import time


def calibrate_menu_command():

    # Shop button
    time.sleep(5)
    pos1 = pyautogui.position()
    pyautogui.click()

    # Deck Button
    time.sleep(4)
    pos2 = pyautogui.position()
    pyautogui.click()

    # Battle Button
    time.sleep(4)
    pos3 = pyautogui.position()
    pyautogui.click()

    f = open("../values/menu-buttons.txt", "w")
    f.write(str(pos1.x) + " " + str(pos1.y) + "\n" + str(pos2.x) + " " + str(pos2.y) + "\n" + str(pos3.x) + " " + str(
        pos3.y))
    f.close()


if __name__ == "__main__":
    calibrate_menu_command()