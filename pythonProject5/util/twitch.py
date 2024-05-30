from twitchio import Message
from twitchio.client import Client
import asyncio
from twitchToken import setup_token, getConfig

def eventLoop():
    print("Helloooo")
    loop.call_later(.5, eventLoop)

loop = asyncio.new_event_loop()
loop.call_later(.5, eventLoop)

# https://twitchio.dev/en/stable/twitchio.html#twitchio.Client.event_message
class Bot(Client):

    def __init__(self):
        # To get more tokens
        # https://id.twitch.tv/oauth2/authorize?response_type=token&client_id=<your client id>&redirect_uri=https://localhost:3000&scope=chat%3Aread+chat%3Aedit
        #
        super().__init__(token=getConfig("token"), initial_channels=['personman61'], loop=loop)

    async def event_ready(self):
        # Notify us when everything is ready!
        # We are logged in and ready to chat and use commands...\
        print("Here we go")
        print(f'Logged in as')
        print(f'User id is | {self.user_id}')

    async def event_message(self, message: Message):
        print(message.author.name + ": " + message.content)



# bot.run() is blocking and will stop execution of any below code here until stopped or closed.

if __name__ == '__main__':
    bot = Bot()
    bot.run()