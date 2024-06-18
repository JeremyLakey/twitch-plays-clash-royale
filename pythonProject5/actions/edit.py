from values.cards import validate_card_name
from util.click import scroll_down, click_image, image_found
import pyautogui
import time

f = open("./values/editDeck.txt", "r")
pos1 = f.readline().split()
pos2 = f.readline().split()


NUM_SCROLL_EDIT_ATTEMPTS = 10

def edit_deck_command(card, slot):
    try:
        remove(slot)
        attempts = NUM_SCROLL_EDIT_ATTEMPTS
        while attempts > 0:
            attempts -= 1
            if image_found(f'./images/cards/{card}.png'):
                click_image(f'./images/cards/{card}.png')
                time.sleep(.7)
                click_image('./images/use.png')
                return True
            scroll_down()
        return False
    except:
        return False
    return False


def parse_edit_command(content: str):

    if content == "skip":
        return content, None

    c = content.split(" ")

    if len(c) == 1:
        return validate_card_name(content), None
    elif len(c) == 2:
        slot = parse_deck_slot(c[1])
        if slot is not None:
            return validate_card_name(c[0]), slot
        else:
            return validate_card_name(c[0] + " " + c[1])
    elif len(c) == 3:
        return validate_card_name(c[0] + " " + c[1]), parse_deck_slot(c[2])

    return None, None


VALID_DECK_SLOTS = ["1", "2", "3", "4", "5", "6", "7", "8"]


def parse_deck_slot(n: str):
    if n in VALID_DECK_SLOTS:
        return n
    return None


def remove(slot):
    if slot == 1:
        remove_1()
    elif slot == 2:
        remove_2()
    elif slot == 3:
        remove_3()
    elif slot == 4:
        remove_4()
    elif slot == 5:
        remove_5()
    elif slot == 6:
        remove_6()
    elif slot == 7:
        remove_7()
    elif slot == 8:
        remove_8()


def remove_1():
    pyautogui.click(pos1.x, pos1.y)


def remove_2():
    pyautogui.click(pos1.x + (pos2.x - pos1.x) * .3, pos1.y)


def remove_3():
    pyautogui.click(pos1.x + (pos2.x - pos1.x) * .6, pos1.y)


def remove_4():
    pyautogui.click(pos2.x, pos1.y)


def remove_5():
    pyautogui.click(pos1.x, pos2.y)


def remove_6():
    pyautogui.click(pos1.x + (pos2.x - pos1.x) * .3, pos2.y)


def remove_7():
    pyautogui.click(pos1.x + (pos2.x - pos1.x) * .6, pos2.y)


def remove_8():
    pyautogui.click(pos2.x, pos2.y)



