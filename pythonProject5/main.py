
from twitchio import Message
from util.twitch import start_bot
from model.game import Game


model = None


def main():
    model.do_action()


def broadcast(message: Message):
    # print(message.author.name + ": " + message.content)
    model.receive_message(message)


if __name__ == "__main__":
    model = Game(debug=True)
    start_bot(main, broadcast)

