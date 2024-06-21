import pyautogui
from util.click import scroll_down, click_image, image_found, click_safespot
from values.cards import validate_card_name
import time



NUM_SCROLL_SHOP_ATTEMPTS = 5
VALID_SHOP_ACTIONS = ["lightning chest", "fortune chest", "kings chest", "skip"]


def do_shop_command(content, model):

    attempts = NUM_SCROLL_SHOP_ATTEMPTS
    while attempts > 0:
        attempts -= 1
        if content in VALID_SHOP_ACTIONS:
            if image_found(f'./images/chests/{content}.png'):
                click_image(f'./images/chests/{content}.png')
                time.wait(.5)
                click_image('./images/gem-shop.png')
                model.loading_screen = True
                return True
        elif image_found(f'./images/cards/{content}.png'):
            click_image(f'./images/cards/{content}.png')
            time.wait(.5)
            click_image('./images/gold-shop.png')
            time.wait(.2)
            click_safespot()
            time.wait(.2)
            click_safespot()
            return True
    return False


def parse_shop_command(content: str):
    if content in VALID_SHOP_ACTIONS:
        return content

    if "lightning" or "lightning chest" or "lighting" or "lighting chest":
        return "lightning chest"
    if "fortune" or "fortune chest":
        return "fortune chest"
    if "kings" or "kings chest" or "king's" or "king's chest" or "king" or "king chest":
        return "kings chest"

    if validate_card_name(content):
        return content

    return None

