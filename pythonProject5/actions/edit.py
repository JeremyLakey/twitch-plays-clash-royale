from values.cards import validate_card_name


def edit_deck_command(card, slot):
    print("Implement edit deck command")
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
