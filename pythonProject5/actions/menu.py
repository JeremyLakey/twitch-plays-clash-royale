
def do_menu_command(command):
    return None


VALID_MENU_ACTIONS = ["battle", "edit", "upgrade", "shop"]


def parse_menu_command(content: str):
    if content in VALID_MENU_ACTIONS:
        return content

    return None
