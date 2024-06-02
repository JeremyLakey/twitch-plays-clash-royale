from twitchio import Message
import time

GAME_STATES = ["main", "battle", "edit-deck", "upgrade-card", "shop"]


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
        self.battleWait = 0         # used to decrement until next command. Each 1 is an action tick (.5 seconds)
        if debug:
            self.all_messages = []


    def receive_message(self, message: Message):
        print(message.author + ": " + message.content)
        if self.debug:
            self.all_messages.append(message)

        if message.author in self.user_submitted:
            return

        self.user_submitted[message.author] = True





    def select_action(self):
        if self.mode == "main":
            return self.main_select_action()

        elif self.mode == "battle":
            return self.main_select_action()

        elif self.mode == "edit-deck":
            return self.edit_deck_select_action()

        elif self.mode == "upgrade-card":
            return self.upgrade_card_select_action()

        elif self.mode == "shop":
            return self.shop_select_action()

        return "implement mode"



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


    def edit_deck_select_action(self):


    def upgrade_card_select_action(self):


    def shop_select_action(self):

