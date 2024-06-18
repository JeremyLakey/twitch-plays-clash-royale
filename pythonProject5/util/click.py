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

f = open("./values/scroll.txt", "r")
scroll_top = f.readline().split()
scroll_bot = f.readline().split()


def scroll_down():
    try:
        pyautogui.moveTo(scroll_top[0], scroll_top[1])
        pyautogui.dragTo(scroll_bot[0], scroll_bot[1], .2)
    except:
        return


f = open("./values/chests.txt", "r")
safespot = f.readline().split()


def click_safespot():
    pyautogui.click(safespot.x, safespot.y)

