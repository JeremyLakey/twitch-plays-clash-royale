import time

import pyautogui
import random
from values.cards import validate_card_name
from values.positions import VALID_POSITIONS
import time


async def play_card(card, pos):
    try:
        print(f"Find ./images/cards/{card}.png")
        location = pyautogui.center(pyautogui.locateOnScreen(f'./images/cards/{card}.png', confidence=.3))
        if location is not None:
            pyautogui.click(x=location.x, y=location.y)
            time.sleep(1)
            pyautogui.press(pos)
            return True
        print("Location is none")
        return False
    except Exception as e:
        print("ERROR finding card: " + str(e))
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
