
VALID_MENU_ACTIONS = ["lightning chest", "fortune chest", "kings chest"]


def do_shop_command(content):
    print("Implement shop command")
    return False


def parse_shop_command(content: str):
    if content in VALID_MENU_ACTIONS:
        return content

    if "lightning" or "lightning chest" or "lighting" or "lighting chest":
        return "lightning chest"
    if "fortune" or "fortune chest":
        return "fortune chest"
    if "kings" or "kings chest" or "king's" or "king's chest" or "king" or "king chest":
        return "kings chest"

    return None

