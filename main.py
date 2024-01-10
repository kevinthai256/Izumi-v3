from lib.bot import bot
from lib.util.info import InfoTemplate
from lib.util.colors import colord
from lib.util.keep_alive import keep_alive
import os
import discord
import json
from discord.ext import commands
import random
from replit import db
from asyncio import sleep
import nekos
from discord.utils import get
import datetime
import atexit
import asyncio
from glob import glob
from lib.util.animeinfo import animesearch

print(animesearch("ImPowiz"))
bot = commands.Bot(command_prefix = '.', intents=discord.Intents.all(),  help_command=None)

def exit_handler():
    print('My application is ending!')
    bot.change_presence(status=discord.Status.idle,          activity=discord.Game("Bot is undergoing matainence/updates; please stand by."))

async def load_extensions():
  COMMANDS = [path.split("/")[-1][:-3] for path in glob("./lib/commands/*.py")]
  for command in COMMANDS:
    await bot.load_extension(f"lib.commands.{command}")
    
async def main():
      async with bot:
        await load_extensions()
        await bot.start(os.environ['token'])

my_secret = os.environ['token']

atexit.register(exit_handler)
keep_alive()

asyncio.run(main())
