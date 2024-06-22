import time

import pyautogui
from twitchio import Message
from actions.emotes import maybe_emote
from actions.help import maybe_help
from actions.play import play_card, parse_play_command
from actions.edit import edit_deck_command, parse_edit_command
from actions.upgrade import upgrade_card_command, parse_upgrade_command
from actions.menu import parse_menu_command, do_menu_command
from actions.shop import parse_shop_command, do_shop_command
from actions.blueStacks import toggle_controls_hints, is_showing_controls
from util.click import image_found, click_image, click_safespot

GAME_STATES = ["main", "battle", "edit-deck", "upgrade-card", "shop"]
MAIN_MENU_WAIT = 20
MENU_COMMANDS_PROMPT = "Type either battle, edit, upgrade, shop"
BATTLE_COMMAND_PROMPT = "Play a card by typing \"<card-name> <position>\""


class Game:
    """
    Function
    Hold game mode
    Hold commands
    Hold timer var for next selecting command
    Holds logic for selecting next overarching command to run
    """
    def __init__(self, debug=False):
        self.mode = "main"
        self.commands = {}          # used to evaluate most voted command
        self.cardPositions = {}     # used to evaluate most voted position for card
        self.user_submitted = {}    # prevent spam
        self.totalCommands = 0      # used to evaluate percentages for waiting command
        self.battleWait = 0
        self.wait = 0               # used to decrement until next command. Each 1 is an action tick (.5 seconds)
        self.loading_screen = False
        self.bot = None
        self.debug = debug
        if debug:
            self.debugFile = open("./logs/log.txt", mode="w")

    def __del__(self):
        if self.debug:
            self.debugFile.close()

    def receive_message(self, message: Message):
        self.debug_log(message.author + ": " + message.content)

        if maybe_emote(message.content):
            return

        if maybe_help(message.content):
            return

        if message.author in self.user_submitted:
            return

        self.user_submitted[message.author] = True

        if self.mode == "main":
            result = parse_menu_command(message.content)

        elif self.mode == "battle":
            card, pos = parse_play_command(message.content)
            if card is not None:
                if card in self.commands:
                    self.commands[card] += 1
                else:
                    self.commands = 1
                if pos is not None:
                    if card in self.cardPositions:
                        if pos in self.cardPositions[card]:
                            self.cardPositions[card][pos] += 1
                        else:
                            self.cardPositions[card][pos] = 1
                    else:
                        self.cardPositions[card] = {}
                        self.cardPositions[card][pos] = 1

        elif self.mode == "edit-deck":
            card, slot = parse_edit_command(message.content)
            if card is not None:
                if card in self.commands:
                    self.commands[card] += 1
                else:
                    self.commands = 1
                if slot is not None:
                    if card in self.cardPositions:
                        if slot in self.cardPositions[card]:
                            self.cardPositions[card][slot] += 1
                        else:
                            self.cardPositions[card][slot] = 1
                    else:
                        self.cardPositions[card] = {}
                        self.cardPositions[card][slot] = 1

        elif self.mode == "upgrade-card":
            card = parse_upgrade_command(message.content)
            if card is not None:
                if card in self.commands:
                    self.commands[card] += 1
                else:
                    self.commands = 1

        elif self.mode == "shop":
            command = parse_shop_command(message.content)
            if command is not None:
                if command in self.commands:
                    self.commands[command] += 1
                else:
                    self.commands = 1

    def reset_commands(self, wait=0):
        self.commands = {}
        self.cardPositions = {}
        self.totalCommands = 0
        self.user_submitted = {}
        self.battleWait = 0
        self.wait = wait

    def do_action(self):
        if self.wait > 0:
            self.wait -= 1
            return

        if self.loading_screen:
            if image_found("./images/menu-swords.png", confidence=.6):
                self.loading_screen = False
                self.reset_commands(MAIN_MENU_WAIT)
                self.mode = "main"
                self.debug_log("In main menu, switching to main mode")
            else:
                click_safespot()
                self.debug_log("Not in main menu, clicking safespot")
                return

        if self.mode == "main":
            if not image_found("./images/menu-swords.png", confidence=.6):
                self.debug_log("Not in menu, clicking safe spot")
                click_safespot()
                return

            do_menu_command(self.main_select_action(), self)
            return

        elif self.mode == "battle":
            if image_found("./images/ok.png", confidence=.7):
                self.debug_log("battle is over")
                # battle is over
                self.loading_screen = True
                self.reset_commands(MAIN_MENU_WAIT)
                self.mode = "main"
                click_image("./images/ok.png", confidence=.7)
                if is_showing_controls():
                    toggle_controls_hints()

                return

            card, pos = self.battle_select_action()
            while card is not None:
                if play_card(card, pos):
                    self.debug_log("Playing " + card + " at " + pos)
                    self.type_to_chat("Play " + card + " at " + pos + ". " + BATTLE_COMMAND_PROMPT)
                    self.reset_commands()
                    return
                card, pos = self.battle_select_action()

        elif self.mode == "edit-deck":
            card, slot = self.edit_deck_select_action()
            while card is not None:
                if edit_deck_command(card, slot):
                    self.type_to_chat("Placing " + card + " into slot " + slot + ". " + MENU_COMMANDS_PROMPT)
                    self.debug_log("Editting deck: " + card + " into " + slot + ".")
                    self.reset_commands()
                    return
                card, slot = self.edit_deck_select_action()
            self.reset_commands()

        elif self.mode == "upgrade-card":
            command = self.upgrade_card_select_action()
            while command is not None:
                if upgrade_card_command(command):
                    self.type_to_chat("Upgrading " + command + ". " + MENU_COMMANDS_PROMPT)
                    self.debug_log("Upgrading " + command + ".")
                    self.reset_commands()
                    return
                command = self.upgrade_card_select_action()

        elif self.mode == "shop":
            command = self.shop_select_action()
            while command is not None:
                if do_shop_command(command, self):
                    self.type_to_chat("Getting " + command + ". " + MENU_COMMANDS_PROMPT)
                    self.debug_log("Buying " + command + ".")
                    self.reset_commands()
                    self.mode == "menu"

                    return
                command = self.shop_select_action()

        print("Implement mode " + self.mode)
        return

    # returns the command
    def main_select_action(self):
        m = 0
        v = None
        for key in self.commands:
            if self.commands[key] > m:
                m = self.commands[key]
                v = key
        self.commands[v] = 0
        return v

    def battle_select_action(self):
        if "wait" in self.commands:
            self.battleWait += 1
            waitLimit = min(.5, (self.battleWait * 5) / 100)
            waitRatio = self.commands["wait"]/self.totalCommands
            if waitRatio > waitLimit:
                return None, None

            self.commands["wait"] = 0

        bsf = 0  # best so far
        card = None
        for key in self.commands:
            if self.commands[key] > bsf:
                bsf = self.commands[key]
                card = key

        # get most voted for position for card
        bsf = 0
        pos = None
        for key in self.cardPositions[card]:
            if self.cardPositions[card][key] > bsf:
                bsf = self.cardPositions[card][key]
                pos = key

        self.commands[card] = 0  # If cannot play card, we will look for the second best thing
        if pos is None:
            pos = "c"  # assume we play in the back
        return card, pos

    def edit_deck_select_action(self):
        if "skip" in self.commands:
            skipRatio = self.commands["skip"]/self.totalCommands
            if skipRatio > .3:
                return None, None

        bsf = 0  # best so far
        card = None
        for key in self.commands:
            if self.commands[key] > bsf:
                bsf = self.commands[key]
                card = key

        # get most voted for position for card
        bsf = 0
        slot = None
        for key in self.cardPositions[card]:
            if self.cardPositions[card][key] > bsf:
                bsf = self.cardPositions[card][key]
                slot = key

        self.commands[card] = 0 # if cannot play card, we will look for the second best thing
        if slot is None:
            slot = "c" # assume we play in the back
        return card, slot

    def upgrade_card_select_action(self):
        bsf = 0  # best so far
        card = None
        for key in self.commands:
            if self.commands[key] > bsf:
                bsf = self.commands[key]
                card = key

        return card

    def shop_select_action(self):
        bsf = 0  # best so far
        command = None
        for key in self.commands:
            if self.commands[key] > bsf:
                bsf = self.commands[key]
                command = key

        return command

    def type_to_chat(self, s):
        if self.bot is not None:
            self.bot.send_to_chat(s)

    def debug_log(self, c):
        if self.debug:
            self.debugFile.write(str(time.time()) + c)
