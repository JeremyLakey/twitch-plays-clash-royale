import pyautogui


def click_image(file, confidence=.9):
    try:
        location = pyautogui.locateOnScreen(file, confidence=confidence)
        x, y = pyautogui.center(location)
        pyautogui.click(x, y)
        return True
    except:
        return False


def image_found(file, confidence=.9):
    try:
        location = pyautogui.locateOnScreen(file, confidence=confidence)
        return location is not None
    except:
        return False


f = open("./values/chests.txt", "r")
safespot = f.readline().split()


def click_safespot():
    pyautogui.click(safespot.x, safespot.y)

