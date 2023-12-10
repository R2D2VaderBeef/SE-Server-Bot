import os
from dotenv import dotenv_values
env = dotenv_values(".env")

import bot
bot.login(env['TOKEN'], env['CHANNEL'])

import logger
logger.attach(env['SERVICE'])