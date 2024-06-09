from values.cards import validate_card_name


def upgrade_card_command(card):
    print("Implement upgrade deck command")
    return False


def parse_upgrade_command(content: str):

    if content == "skip":
        return content

    return validate_card_name(content)
