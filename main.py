import os
import threading
from dotenv import dotenv_values
env = dotenv_values(".env")

import bot
bot_thread = threading.Thread(target=bot.login, args=(env['TOKEN'], env['CHANNEL']))
bot_thread.start()

import logger
logger_thread = threading.Thread(target=logger.attach, args=(env['SERVICE']))
logger_thread.start()