from model.game import Game
from twitchio import Message


def maybe_help(message: Message):
    if message == "help":
        send_whisper(message)
        return True
    return False


async def send_whisper(message: Message):
    message.author.channel().send("You asked for help, Ask me to implement help")
