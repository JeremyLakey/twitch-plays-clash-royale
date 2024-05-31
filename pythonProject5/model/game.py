from twitchio import Message


class Game:

    def __init__(self):
        self.mode = "main"
        self.commands = {}
        self.all_messages

    def receive_message(self, message: Message):
        print(message.author + ": " + message.content)
        self.all_messages.append(message)

