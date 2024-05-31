from actions.emotes import maybe_emote
from twitchio import Message
from util.twitch import start_bot


model = None


def main():
    print("Hmmmm..")

def broadcast(message: Message):
    print(message.author.name + ": " + message.content)
    if maybe_emote(message.content):
        return


if __name__ == "__main__":
    start_bot(main, broadcast)

