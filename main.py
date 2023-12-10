import os
from dotenv import load_dotenv
load_dotenv()

import bot
bot.login(os.environ['TOKEN'], os.environ['CHANNEL'])

import logger
logger.attach(os.environ['SERVICE'])