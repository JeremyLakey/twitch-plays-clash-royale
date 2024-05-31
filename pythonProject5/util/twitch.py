from twitchio import Message
from twitchio.client import Client
from util.config import getConfig
import asyncio

MAIN_LOOP_DELAY = 2


def event_loop():
    global loop, loop_main_function
    loop_main_function()
    loop.call_later(MAIN_LOOP_DELAY, event_loop)


loop_main_function = None
loop = asyncio.new_event_loop()


def start_bot(main, broadcast):
    global loop, loop_main_function
    loop_main_function = main
    loop.call_later(MAIN_LOOP_DELAY, event_loop)
    bot = Bot(loop, broadcast)

    # bot.run() is blocking and will stop execution of any below code here until stopped or closed.
    bot.run()


# https://twitchio.dev/en/stable/twitchio.html#twitchio.Client.event_message
class Bot(Client):

    def __init__(self, loop, broadcast):
        # To get more tokens
        # https://id.twitch.tv/oauth2/authorize?response_type=token&client_id=<your client id>&redirect_uri=https://localhost:3000&scope=chat%3Aread+chat%3Aedit
        #
        super().__init__(token=getConfig("token"), initial_channels=['personman61'], loop=loop)
        self.broadcast = broadcast

    async def event_ready(self):
        # Notify us when everything is ready!
        # We are logged in and ready to chat and use commands...\
        print("Here we go")
        print(f'Logged in as')
        print(f'User id is | {self.user_id}')

    async def event_message(self, message: Message):
        self.broadcast(message)


