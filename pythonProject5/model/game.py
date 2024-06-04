from twitchio import Message
from actions.play import play_card
from actions.edit import edit_deck_command

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
        self.battleWait = 0
        self.wait = 0 # used to decrement until next command. Each 1 is an action tick (.5 seconds)
        if debug:
            self.all_messages = []


    def receive_message(self, message: Message):
        print(message.author + ": " + message.content)
        if self.debug:
            self.all_messages.append(message)

        if message.author in self.user_submitted:
            return

        self.user_submitted[message.author] = True


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

        if self.mode == "main":
            return self.main_select_action()

        elif self.mode == "battle":
            card, pos = self.battle_select_action()
            while card is not None:
                if play_card(card, pos):
                    self.reset_commands()
                    return
                card, pos = self.battle_select_action()

        elif self.mode == "edit-deck":
            card, slot = self.edit_deck_select_action()
            while card is not None:
                if edit_deck_command(card, slot):
                    self.reset_commands()
                    return
                card, slot = self.edit_deck_select_action()
            self.reset_commands()

        elif self.mode == "upgrade-card":
            self.upgrade_card_select_action()

        elif self.mode == "shop":
            self.shop_select_action()

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
            waitLimit = min(.5, (self.battleWait * 5) / 100)
            waitRaito = self.commands["wait"]/self.totalCommands
            if waitRaito > waitLimit:
                return None, None

            self.commands["wait"] = 0

        bsf = 0 # best so far
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

        self.commands[card] = 0 # if cannot play card, we will look for the second best thing
        if pos is None:
            pos = "c" # assume we play in the back
        return card, pos


    def edit_deck_select_action(self):
        if "skip" in self.commands:
            skipRaito = self.commands["skip"]/self.totalCommands
            if skipRaito > .3:
                return None, None

        bsf = 0 # best so far
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


    def shop_select_action(self):

