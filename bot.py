import discord

channel_id = None
channel = None

class DiscordBot(discord.Client):
    async def on_ready(self):
        global channel
        channel = client.get_channel(int(channel_id))

intents = discord.Intents.default()
intents.message_content = True
client = DiscordBot(intents=intents)

def login(token, new_channel_id):
    global channel_id
    channel_id = new_channel_id
    client.run(token)

async def log_line(message):
    await channel.send(message)