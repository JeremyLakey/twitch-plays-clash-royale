import pyautogui
import random
from values.cards import validate_card_name
from values.positions import  VALID_POSITIONS


def play_card(card, pos):
    try:
        location = pyautogui.center(pyautogui.locateOnScreen(f'./images/cards/{card}.png'))
        if location is not None:
            pyautogui.click(location.x, location.y)
            pyautogui.press(pos)
            return True
        return False
    except:
        return False


# returns tuple of troop name and card
# returns None in 0 index on parse failure
def parse_play_command(content: str):
    c = content.lower().split(" ")
    if len(c) == 1:
        return validate_card_name(c[0]), None
    elif len(c) == 2:
        pos = validate_position(c[1])
        if pos is not None:
            card = validate_card_name(c[0])
            return card, validate_position(c[1])
        else:
            return validate_card_name(content), None
    elif len(c) == 3:
        pos = validate_position(c[2])
        if pos is not None:
            card = validate_card_name(c[0] + " " + c[1])
            return card, c[2]

    return None, None


def validate_position(pos):
    if pos in VALID_POSITIONS:
        return True
    if pos == "bridge":
        return random.choice(["n", "s"])
    if pos == "back":
        return random.choice(["c", "d"])
    if pos == "tower":
        return random.choice(["y", "z"])
    if pos == "random":
        return random.choice(VALID_POSITIONS)
    return False
