

import pyautogui


def click_image(file):
    try:
        location = pyautogui.locateOnScreen(file)
        location.center
        return True
    except:
        return False
