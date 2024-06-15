from model.game import Game
from actions.blueStacks import *
import pyautogui

f = open("./values/menu-buttons.txt", "r")
shopButton = f.readline().split()
deckButton = f.readline().split()
battleButton = f.readline().split()


def do_menu_command(command, model: Game):
    if command is None:
        model.reset_commands(10)

    if command == "battle":
        set_up_battle(model)

    elif command == "edit":
        set_up_edit(model)

    elif command == "upgrade":
        set_up_upgrade(model)

    elif command == "shop":
        set_up_shop(model)

    return


VALID_MENU_ACTIONS = ["battle", "edit", "upgrade", "shop"]


def parse_menu_command(content: str):
    if content in VALID_MENU_ACTIONS:
        return content

    return None


def set_up_battle(model):
    model.reset_commands(10)
    model.mode = "battle"

    pyautogui.click(battleButton[0], battleButton[1])

    if not is_showing_controls():
        toggle_controls_hints()


def set_up_edit(model):
    model.reset_commands(30)
    model.mode = "edit-deck"

    pyautogui.click(deckButton[0], deckButton[1])

    if is_showing_controls():
        toggle_controls_hints()


def set_up_upgrade(model):
    model.reset_commands(30)
    model.mode = "upgrade-card"

    pyautogui.click(deckButton[0], deckButton[1])

    if is_showing_controls():
        toggle_controls_hints()


def set_up_shop(model):
    model.reset_commands(30)
    model.mode = "shop"

    pyautogui.click((shopButton[0]), shopButton[1])

    if is_showing_controls():
        toggle_controls_hints()



