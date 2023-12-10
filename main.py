import os
from dotenv import load_dotenv
load_dotenv()

import discord
import logger

channel = None

class DiscordBot(discord.Client):
    async def on_ready(self):
        global channel
        channel = client.get_channel(int(os.getenv["CHANNEL"]))
        logger.attach()

intents = discord.Intents.default()
intents.message_content = True
client = DiscordBot(intents=intents)

def login():
    client.run(os.getenv['TOKEN'])

async def log_line(message):
    await channel.send(message)

login()