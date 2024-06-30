import pyautogui
from util.click import click_image

f = open("./values/chests.txt", "r")
chest1 = f.readline().split()
chest2 = f.readline().split()
chest3 = f.readline().split()
chest4 = f.readline().split()
unlockButton = f.readline().split()


def do_unlock_command(command, model):
    if click_image("./images/open-chest.png"):
        model.loading_screen = True
        return True

    if "1":
        pyautogui.click(chest1[0], chest1[1])
        pyautogui.click(unlockButton[0], unlockButton[1])
        return True
    elif "2":
        pyautogui.click(chest2[0], chest2[1])
        pyautogui.click(unlockButton[0], unlockButton[1])
        return True
    elif "3":
        pyautogui.click(chest3[0], chest3[1])
        pyautogui.click(unlockButton[0], unlockButton[1])
        return True
    elif "4":
        pyautogui.click(chest4[0], chest4[1])
        pyautogui.click(unlockButton[0], unlockButton[1])
        return True

    return False


VALID_UNLOCK_ACTIONS = ["1", "2", "3", "4"]


def parse_unlock_command(content: str):
    if content in VALID_UNLOCK_ACTIONS:
        return content

    return None
