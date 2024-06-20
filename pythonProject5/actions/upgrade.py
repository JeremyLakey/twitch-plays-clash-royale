import time
from values.cards import validate_card_name
from util.click import click_image, image_found, scroll_down, click_safespot

NUM_SCROLL_UPGRADE_ATTEMPTS = 10


def upgrade_card_command(card):
    try:
        attempts = NUM_SCROLL_UPGRADE_ATTEMPTS
        while attempts > 0:
            attempts -= 1
            if image_found(f'./images/cards/{card}.png'):
                click_image(f'./images/cards/{card}.png')
                time.sleep(.7)
                click_image('./images/upgrade.png')
                time.sleep(.7)
                click_image('./images/upgrade.png')
                time.sleep(.7)
                if image_found('./images/confirm.png'):
                    click_image(f'./images/cards/{card}.png')
                    time.sleep(5)
                    click_safespot()
                    time.sleep(.7)
                    click_safespot()
                    time.sleep(.7)
                    click_safespot()
                else:
                    click_safespot()
                    time.sleep(.7)
                    click_safespot()
                    time.sleep(.7)
                    click_safespot()
                    time.sleep(.7)
                    click_safespot()
                return True
            scroll_down()
        return False
    except:
        return False
    return False
    return False


def parse_upgrade_command(content: str):

    if content == "skip":
        return content

    return validate_card_name(content)
