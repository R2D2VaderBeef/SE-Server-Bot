import os
from dotenv import load_dotenv
load_dotenv()
import threading
import asyncio

import discord
import logger

channel = None

class DiscordBot(discord.Client):
    async def on_ready(self):
        global channel
        channel = client.get_channel(int(os.getenv('CHANNEL')))
        logger_thread = threading.Thread(target=logger.attach, args=(log_line,))
        logger_thread.start()

intents = discord.Intents.default()
intents.message_content = True
client = DiscordBot(intents=intents)

def login():
    client.run(os.getenv('TOKEN'))

def log_line(message):
    asyncio.get_event_loop().create_task(send_log_message(message)) 

async def send_log_message(message):
    channel.send(message)

login()