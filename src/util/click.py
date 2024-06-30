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
        pyautogui.moveTo(int(scroll_top[0]), int(scroll_top[1]))
        pyautogui.dragTo(int(scroll_bot[0]), int(scroll_bot[1]), .2)
    except:
        return


f = open("./values/safespot.txt", "r")
safespot = f.readline().split()


def click_safespot():
    global safespot
    pyautogui.click(int(safespot[0]), int(safespot[1]))

