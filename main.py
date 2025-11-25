from lib.bot import bot
from lib.util.info import InfoTemplate
from lib.util.colors import colord
from lib.util.keep_alive import keep_alive
import os
import discord
import json
from discord.ext import commands
import random
from asyncio import sleep
from discord.utils import get
import datetime
import atexit
import asyncio
from glob import glob
from dotenv import load_dotenv

load_dotenv()

bot = commands.Bot(command_prefix = '.', intents=discord.Intents.all(),  help_command=None)

def exit_handler():
    print('My application is ending!')

async def load_extensions():
  COMMANDS = [
    os.path.basename(path)[:-3] 
    for path in glob("./lib/commands/*.py") 
    if not path.endswith("__init__.py")
]
  for command in COMMANDS:
    await bot.load_extension(f"lib.commands.{command}")
    
async def main():
      async with bot:
        await load_extensions()
        await bot.start(os.environ['DISCORD_API_KEY'])

atexit.register(exit_handler)
keep_alive()

asyncio.run(main())
