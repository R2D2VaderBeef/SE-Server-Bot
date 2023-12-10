import os
from dotenv import load_dotenv
load_dotenv()
import asyncio

import discord

import select
from systemd import journal

channel = None

class DiscordBot(discord.Client):
    async def on_ready(self):
        global channel
        channel = client.get_channel(int(os.getenv('CHANNEL')))
        self.loop.create_task(self.attach())

    def attach(*args):
        j = journal.Reader()
        j.log_level(journal.LOG_INFO)

        j.add_match(_SYSTEMD_UNIT=os.getenv('SERVICE'))
        j.seek_tail()
        j.get_previous()

        p = select.poll()
        p.register(j, j.get_events())

        while p.poll():
            if j.process() != journal.APPEND:
                continue

            for entry in j:
                if entry['MESSAGE'] != "":
                    #str(entry['__REALTIME_TIMESTAMP'] )+ ' ' +
                    print(entry['MESSAGE'])
                    asyncio.get_event_loop().create_task(log_line(entry['MESSAGE']))

intents = discord.Intents.default()
intents.message_content = True
client = DiscordBot(intents=intents)

def login():
    client.run(os.getenv('TOKEN'))

async def log_line(message):
    await channel.send(message) 

login()